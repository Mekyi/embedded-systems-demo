import paho.mqtt.client as mqtt
import os
import time
import json
from sense_hat import SenseHat


# Constants
PATH = os.path.dirname(os.path.abspath(__file__))
INTERVAL = 60 # Message publish interval (seconds)

# MQTT client config
GATEWAY_ID = os.environ['GATEWAY_ID']
HOST = os.environ['HOST']
PORT = 443
CREDENTIALS = {
    'USER': os.environ['USER'],
    'PASS': os.environ['PASSWORD']
}


# SenseHAT sensor object
def get_sensehat_data():
    orientation = sense.get_orientation_degrees()
    rotation = sense.get_gyroscope_raw()
    acceleration = sense.get_accelerometer_raw()

    sensehat_data = {
        'sensors': [
            {
                'key': 'temperature',
                'value': sense.get_temperature()
            },
            {
                'key': 'humidity',
                'value': sense.get_humidity()
            },
            {
                'key': 'pressure',
                'value': sense.get_pressure()
            },
            {
                'key': 'compass',
                'value': sense.get_compass()
            },
            {
                'key': 'orientation_pitch',
                'value': orientation['pitch']
            },
            {
                'key': 'orientation_roll',
                'value': orientation['roll']
            },
            {
                'key': 'orientation_yaw',
                'value': orientation['yaw']
            },
            {
                'key': 'rotation_x',
                'value': rotation['x']
            },
            {
                'key': 'rotation_y',
                'value': rotation['y']
            },
            {
                'key': 'rotation_z',
                'value': rotation['z']
            },
            {
                'key': 'acceleration_x',
                'value': acceleration['x']
            },
            {
                'key': 'acceleration_y',
                'value': acceleration['y']
            },
            {
                'key': 'acceleration_z',
                'value': acceleration['z']
            }
        ]
    }

    return sensehat_data

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print(f'Connected to broker with result code: {rc}')

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Disconnected')
    else:
        print('Unexpected disconnection')

def on_publish(client, userdata, mid):
    print('Message published')
    
def on_log(client, userdata, level, buf):
    print(f'Log: {buf}')


# Create MQTT client and attach callback functions
client = mqtt.Client(transport='websockets')
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_log = on_log

# Configure MQTT client
client.tls_set('/etc/ssl/certs/DST_Root_CA_X3.pem')
client.username_pw_set(CREDENTIALS['USER'], CREDENTIALS['PASS'])
client.ws_set_options(path='/mqtt/')

# Initialize Sense Hat
sense = SenseHat()

# Connect to MQTT broker
print(f"Connecting to {HOST}:{PORT} with user {CREDENTIALS['USER']}...")
client.connect(HOST, PORT)

# MQTT client loop to handle message buffers and reconnects
client.loop_start()

# Program loop
while True:
    client.publish(f'{GATEWAY_ID}/sensehat', json.dumps(get_sensehat_data()))
    time.sleep(INTERVAL)

client.loop_stop()