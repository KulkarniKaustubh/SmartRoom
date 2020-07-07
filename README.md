# SmartRoom

##### Final product description

A Raspberry Pi is used along with relays to different devices. Currently, an RGB light is connected to the Raspi. As a person enters the room, the camera detects if it is a known person entering the room. If it is, it checks with an existing API (using polling) for that person's light settings (whether the light is red, green or blue, and whether the light is supposed to be on or off). The user can control his/her settings from the mobile app and they are automatically saved to the API. This enables real time switching on/off of the light and change in color of the light. To check if this recognized individual enters the room, IR sensors are used. Once they are inside the room, the light is switched on/off based on the settings. If more than one person enters the room, the lights will stay on until the last person inside the room leaves.

## Applications

Applications used to communicate to the Raspberry Pi.

## FaceRecognition

Code to recognize faces.

## RaspiFiles

Code that should run on the Raspberry Pi for successful communication.

## Server

Code running on a machine/dedicated server.
