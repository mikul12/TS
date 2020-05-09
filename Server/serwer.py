from flask import Flask, jsonify, request, render_template, abort
from flask_socketio import SocketIO
import simplejson as json
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')
    
#@app.route('/measurements', methods=['GET'])
#def get_measurements():
    #url = "https://tsapipl.azurewebsites.net/api/Measurements"
    #headers = {'Content-type': 'application/json'}
    #response = requests.get(url, headers=headers)
   # data = json.loads(response.text)
    #return {"data": data}
	
#@app.route('/measurements/<int:m_id>', methods=['GET'])
#def get_measurement(m_id):
    #url = "https://tsapipl.azurewebsites.net/api/Measurements/"+str(m_id)
    #headers = {'Content-type': 'application/json'}
    #response = requests.get(url, headers=headers)
    #data = json.loads(response.text)
    #if 'status' is data and data.status == "404":
    #    abort(404)
    #return {"data": data}
	
@app.route('/measurements', methods=['POST'])
def create_measurements():
    if not request.json or not 'Id' in request.json or not 'carsDetected' in request.json or not 'dateTime' in request.json:
        abort(400)
    url = "https://scfm6o72n5.execute-api.us-east-2.amazonaws.com/API/measurement"
    headers = {'Content-type': 'application/json'}
    crowd = (int(request.json['carsDetected']) * 18)
    if crowd>100:
        crowd = 100
    carsDetected = request.json['carsDetected']
    Id = request.json['Id']   
    datetime = request.json['dateTime']     
    body = {
            "Id": Id,
            "carsDetected": str(carsDetected),
            "datetime": datetime,
            "crowd": str(crowd)
    }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    data = json.loads(response.text)
    if 'status' in data:
        abort(data['status'])
    socketio.emit('message', body, broadcast=True)
    return {"data": data}

# @app.route('/containers/json', methods=['GET'])
# def get_containers():
#     r = (requests.get('http://localhost:2375/containers/json'))
#     return jsonify({'response': r.text})
    
# @app.route('/containers/create', methods=['POST'])
# def create_container():
#     r = str(requests.post(url = 'http://localhost:2375/containers/create', data = request.data, headers = {'Content-Type':'application/json'}))
#     return jsonify({'response': r})
    
# @app.route('/containers/<string:container_id>/kill', methods=['POST'])
# def kill_container(container_id):
#     r = str(requests.post('http://localhost:2375/containers/'+container_id+'/kill'))
#     return jsonify({'response': r})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
