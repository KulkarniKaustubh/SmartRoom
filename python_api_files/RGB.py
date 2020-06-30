import RPi.GPIO as GPIO
import requests
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 25
GREEN = 24
BLUE = 23

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

try:
    while (True):

        request = int(input("RGB—>"))
        if(request == 1):
            GPIO.output(RED,GPIO.HIGH)
            GPIO.output(BLUE, GPIO.LOW)
            GPIO.output(GREEN, GPIO.LOW)
        if(request == 2):
            GPIO.output(GREEN,GPIO.HIGH)
            GPIO.output(BLUE, GPIO.LOW)
            GPIO.output(RED, GPIO.LOW)
        if(request == 3):
            GPIO.output(BLUE,GPIO.HIGH)
            GPIO.output(GREEN, GPIO.LOW)
            GPIO.output(RED, GPIO.LOW)


except KeyboardInterrupt:
    GPIO.cleanup()
