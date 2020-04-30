import face_recognition as fr
import os
import cv2
import numpy as np
from PIL import Image
import pickle

def read (filename):
    file = open(filename, 'rb')
    temp_list = pickle.load(file)
    file.close()
    return temp_list

UNKNOWN_FACES_DIR = "unknown_faces"
PROCESSED = "processed"
TOLERANCE = 0.5  #default would be 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 1
MODEL = "hog"  #convolutional is best for image processing and face_recognition #hog is less accurate but the fastest algorithm
ino = 0


known_faces = read('./data/encoded_faces.data')
known_names = read('./data/encoded_names.data')

new = "_smaller"

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


print ("Processing unknown faces...")

for filename in os.listdir(UNKNOWN_FACES_DIR):
    tempImage = Image.open(f"{UNKNOWN_FACES_DIR}/{filename}")
    (file, ext) = os.path.splitext(filename)
    tempImage.thumbnail((600, 600), Image.ANTIALIAS)
    tempImage.save(f"{UNKNOWN_FACES_DIR}/{filename}{new}{ext}", dpi=(600, 600))
    ino = ino + 1
    print ("Image number: ", ino)
    image = fr.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}{new}{ext}")
    os.remove(f"{UNKNOWN_FACES_DIR}/{filename}{new}{ext}")

    loc = face_cascade.detectMultiScale(image, 1.5, 5)
    locations = []
    for (x, y, w, h) in loc:
        locations.append((y, x+w, y+h, x))

    encodings = fr.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        recognized = []
        index = -1
        for face in known_faces:
            results = fr.compare_faces(face, face_encoding, TOLERANCE)
            index = index + 1
            match = None
            # print (results)

            if True in results:
                match = known_names[index]
                # print (f"Match found: {match}")

                top_left = (face_location[3]-5, face_location[0]-10)     #fr.face_locations sends coordinates top, right, bottom, left, in that order
                bottom_right = (face_location[1]+10, face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                top_left = (face_location[3]-20, face_location[2])
                bottom_right = (face_location[1]+30, face_location[2]+20)
                color = [0, 0, 0]
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                # cv2.imread(image)
                cv2.putText(image,
                            match,
                            (face_location[3]-10, face_location[2]+15),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (200, 200, 200),
                            FONT_THICKNESS)
                break

    # cv2.imshow(filename, image)
    # cv2.waitKey(0)
    # cv2.waitKey(10000)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    Image.fromarray(image).save(f"{PROCESSED}/{filename}")
    # break
    # cv2.destroyWindow(filename)

for file in os.listdir(f"{PROCESSED}"):
    img = Image.open(f"{PROCESSED}/{file}")
    img.show()
