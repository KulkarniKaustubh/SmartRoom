import RPi.GPIO as GPIO
import requests
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

API_URL = 'https://6c43cf0b82b1.ngrok.io/users'
RED = 25
GREEN = 24
BLUE = 23

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

def redLight():
    GPIO.output(RED,GPIO.HIGH)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)

def blueLight():
    GPIO.output(GREEN,GPIO.HIGH)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def greenLight():
    GPIO.output(BLUE,GPIO.HIGH)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

response = requests.get(API_URL)

if (response.status_code == 200):
    prevList = response.json()
else:
    print("Error ", response.status_code)

try:
    while True:
        response = requests.get(API_URL)

        # print (response.status_code)

        list = response.json()

        # print (list)

        if (list == prevList):
            print("same, continuing")
            continue
        else:
            prevList = list

        user = list[0]

        if (user['light_on']):
            color = user['light_color']
            if (color == 'red'):
                redLight()
            if (color == 'blue'):
                blueLight()
            if (color == 'green'):
                greenLight()

except KeyboardInterrupt:
    GPIO.cleanup()
