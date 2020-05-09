import os
import pika
import time
import io
import requests
import simplejson as json
import csv
import boto3
from datetime import datetime, timedelta



print('Consumer has been started.')
notConnected = True

while notConnected:
    time.sleep(5)
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', "5672", "/", pika.PlainCredentials('guest', 'guest')))
        #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    except:
        print('Consumer: Cannot connect to rabbit!')
    else:
        notConnected = False
        print('Consumer: Connected to rabbit.')

channel = connection.channel()
channel.queue_declare(queue='images')

index = 1;

def object_detection(image):
    print('Consumer: Detection started.')
    
    with open('credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]
            
    photo = image
    client = boto3.client('rekognition', region_name='eu-west-2', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

    response = client.detect_labels(Image={'Bytes': image}, MaxLabels=10)

    detection_vehicles = []
    for label in response['Labels']:
        if label['Name'] == "Car" or label['Name'] == "Vehicle" or label['Name'] == "Bus" or label['Name'] == "Automobile" or label['Name'] == "Truck" or label['Name'] == "Bike" or label['Name'] == "Scooter" or label['Name'] == "Motorcycle":
            detection_vehicles.append(label['Name'])
    print(detection_vehicles)
    
    return(detection_vehicles)


def send_detection_result(detections_info, highwayId):
    url = "http://server:5000/measurements"  
    headers = {'Content-type': 'application/json'}
    datetimenow = str(datetime.now() + timedelta(hours=1))
    data = {"Id": str(highwayId),
            "carsDetected": str(len(detections_info)),
            "dateTime": str(datetimenow)}
    
    try_number = 0
    while try_number < 3:
        try_number += 1
        try:
            r = requests.post(url, data=json.dumps(data), headers=headers)
        except:
            print('Consumer: Cannot send message to serwer API! Left '+str(3-try_number)+" tries.")
            time.sleep(5)
        else:
            try_number = 3
            print("Consumer: Sent detection result from highway " + highwayId + ".")

def callback(ch, method, properties, body):
    global index
    if body:
        highwayId = str(body)[-6:-1]
        print("Consumer: Received image "+str(index)+" from highway: "+highwayId+".")
        index += 1
        ch.basic_ack(delivery_tag=method.delivery_tag)
        detection_result = object_detection(body)
        send_detection_result(detection_result, highwayId)
    else:
        print('Consumer: Queue empty!')
    time.sleep(3)
    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='images', on_message_callback=callback)
channel.start_consuming()