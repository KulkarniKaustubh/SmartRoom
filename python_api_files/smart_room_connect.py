import requests
import json
import time
# import RPi.GPIO

refreshRate = 2

# while True:
response = requests.get('http://6d0b2099449c.ngrok.io/users')

print (response.status_code)
list = response.json()
print (list)

# time.sleep(refreshRate)
