#training and testing being done in the same file
#no resizing and optimization of images
#will require a good GPU, better if CUDA enabled

import face_recognition as fr
import os
import cv2
from PIL import Image

KNOWN_FACES_DIR = "../known_faces"
UNKNOWN_FACES_DIR = "../unknown_faces"
TOLERANCE = 0.6
FRAME = 3
FONT = 2
MODEL = "cnn"  #convolutional is best for image processing and face_recognition

print ("Loading known faces...")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = fr.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encoding = fr.face_encodings(image)[0]
        print (filename, ":", len(encoding))
        # print (len(encoding))
        known_faces.append(encoding)
        known_names.append(name)

print ("Processing unknown faces...")

for filename in os.listdir(UNKNOWN_FACES_DIR):
    # print (filename)
    image = fr.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    locations = fr.face_locations(image, model=MODEL)
    encodings = fr.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        results = fr.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print (f"Match found: {match}")

            top_left = (face_location[3], face_location[0])     #fr.face_locations sends coordinates top, right, bottom, left, in that order
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            color = [0, 0, 255]
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            # cv2.imread(image)
            cv2.putText(image,
                        match,
                        (face_location[3]+10, face_location[2]+15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (200, 200, 200),
                        FONT)
            cv2.imshow(filename, image)
            cv2.waitKey(0)
            # cv2.waitKey(10000)
            cv2.destroyWindow(filename) #might not work on some ubuntu systems
