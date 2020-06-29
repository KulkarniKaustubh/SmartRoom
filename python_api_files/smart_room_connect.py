import requests
import json
import time
# import RPi.GPIO

refreshRate = 2

prevList = []

while True:
    response = requests.get('http://620854884fa3.ngrok.io/users')

    print (response.status_code)
    list = response.json()
    print (list)

    time.sleep(refreshRate)
