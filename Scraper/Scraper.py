import pika
import time
import requests
import sys
import os

cam_url = os.getenv('cam_url', '')
cam_id = os.getenv('cam_id', '')

#cam_url = 'https://ie.trafficland.com/v2.0/200021/full?system=ddot&pubtoken=d13801625db2774182ed2c03aa6b2facd690ba9792b36a626fb90781c8a164d7&refreshRate=2000&t=1587403539859'
#cam_id = 'CAM1'

print('Scraper has been started.')
print('Cam URL: ', cam_url)
print('Cam ID: ',cam_id)

def getImages(link,highwayID,amountOfImages,timeBetweenRequest):
    notConnected = True

    while notConnected:
        time.sleep(5)
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', "5672", "/", pika.PlainCredentials('guest', 'guest')))
            #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        except:
            print('Cannot connect to rabbit!')
        else:
            notConnected = False
            print('Connected to rabbit.')


    channel = connection.channel()
    channel.queue_declare(queue='images')

    for i in range(0,amountOfImages):
        result = requests.get(link).content
        result = result+highwayID.encode()
        # print(result+highwayID.encode());
        print("Scraper: Image "+str(i+1) +" has been received from WebCam!")
        time.sleep(timeBetweenRequest)
        channel.basic_publish(exchange='',routing_key='images',body=result,properties=pika.BasicProperties(delivery_mode=2,))
        print('Scraper: Message has been sent to queue.')

        time.sleep(2)

    connection.close()

getImages(cam_url,cam_id,500,5)





