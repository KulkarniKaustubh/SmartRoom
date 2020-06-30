import paho.mqtt.publish as publish
import json
import pickle

def write (known, filename):
    file = open(filename, 'wb+')
    pickle.dump(known, file)
    file.close()

def read (filename):
    file = open(filename, 'rb')
    temp_list = pickle.load(file)
    file.close()
    return temp_list

# file = open("/home/kaustubh/Stuff/FaceRecognition/data/encoded_faces.data", rb')

face_list = read("/home/kaustubh/Stuff/FaceRecognition/data/encoded_faces.data")

for i in range(len(face_list)):
    if len(face_list[i]) != 0:
        face_list[i][0] = face_list[i][0].tolist()

publish.single("kaus/users/face_encodings", json.dumps(face_list), hostname="test.mosquitto.org")

print ("Done")
