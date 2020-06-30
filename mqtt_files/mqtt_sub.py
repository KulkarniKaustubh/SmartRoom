import paho.mqtt.client as mqtt
import time
import json
import ssl

connected = False
BROKER_ENDPOINT = "industrial.api.ubidots.com"
TSL_PORT = 8883
MQTT_USERANME = "vishwas"
MQTT_PASSWORD = "Pokemon@2001"
TLS_CERT_PATH = "/Users/vishwasgautam/Desktop/IoT/industrial.cert"


def on_connect(client, userata, flags, rc):

    if (rc == 0):
        print("Connected with code: " + str(rc))
        global connected
        connected = True
    else:
        print("Error connecting")

    client.subscribe("HomeAutomation/light")
    client.subscribe("HomeAutomation/cooler")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
