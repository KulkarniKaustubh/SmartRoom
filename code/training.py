import face_recognition as fr
import os
import cv2
import numpy as np
from PIL import Image
import pickle

def write (known, filename):
    file = open(filename, 'wb+')
    pickle.dump(known, file)
    file.close()

KNOWN_FACES_DIR = "../known_faces"
new = "_smaller"

known_faces = []
known_names = []

print ("Loading known faces...")

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        tempImage = Image.open(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        (file, ext) = os.path.splitext(filename)
        # print (file)
        # print (ext)
        tempImage.thumbnail((600, 600), Image.ANTIALIAS)
        # tempImage = tempImage.resize((1000, 1000), Image.ANTIALIAS)
        tempImage.save(f"{KNOWN_FACES_DIR}/{name}/{file}{new}{ext}", dpi=(600, 600))
        image = fr.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{file}{new}{ext}")
        os.remove(f"{KNOWN_FACES_DIR}/{name}/{file}{new}{ext}")
        encoding = fr.face_encodings(image)
        # print (filename, ":", np.shape(encoding))
        known_faces.append(encoding)
        known_names.append(name)

write (known_faces, '../data/encoded_faces.data')
write (known_names, '../data/encoded_names.data')
