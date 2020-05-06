import pickle
import face_recognition as fr
import cv2
import os
from PIL import Image
import sys, getopt, os

def write (known, filename):
    file = open(filename, 'wb+')
    pickle.dump(known, file)
    file.close()

def read (filename):
    file = open(filename, 'rb')
    temp_list = pickle.load(file)
    file.close()
    return temp_list

def detectFace(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    loc = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
    ).detectMultiScale(gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(1,1))
    locations = []
    for (x, y, w, h) in loc:
        locations.append((y, x+w, y+h, x))
    # print (locations)
    return locations

def recognizeFace(image, locations, datapath):

    known_faces = read(f'{datapath}/encoded_faces.data')
    known_names = read(f'{datapath}/encoded_names.data')
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encodings = fr.face_encodings(rgb, locations)

    TOLERANCE = 0.5
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 1

    for face_encoding, face_location in zip(encodings, locations):
        recognized = []
        index = -1

        for face in known_faces:
            results = fr.compare_faces(face, face_encoding, TOLERANCE)
            index = index + 1
            match = None

            if True in results:
                match = known_names[index]

                top_left = (face_location[3]-5, face_location[0]-10)     #top, right, bottom, left
                bottom_right = (face_location[1]+10, face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                top_left = (face_location[3]-20, face_location[2])
                bottom_right = (face_location[1]+30, face_location[2]+20)
                color = [0, 0, 0]
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image,
                            match,
                            (face_location[3]-10, face_location[2]+15),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (200, 200, 200),
                            FONT_THICKNESS)
                break

def trainModelOptimized(known_directory, data_directory):

    known_faces = []
    known_names = []
    new = "_smaller"

    for name in os.listdir(known_directory):
        for filename in os.listdir(f"{known_directory}/{name}"):
            tempImage = Image.open(f"{known_directory}/{name}/{filename}")
            (file, ext) = os.path.splitext(filename)
            tempImage.thumbnail((600, 600), Image.ANTIALIAS)
            tempImage.save(f"{known_directory}/{name}/{file}{new}{ext}", dpi=(600, 600))
            image = fr.load_image_file(f"{known_directory}/{name}/{file}{new}{ext}")
            os.remove(f"{known_directory}/{name}/{file}{new}{ext}")
            encoding = fr.face_encodings(image)
            known_faces.append(encoding)
            known_names.append(name)

    write (known_faces, f'{data_directory}/encoded_faces.data')
    write (known_names, f'{data_directory}/encoded_names.data')

def getDataPath():
    datapath =''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:", ["data="])
        options = list(opt[0] for opt in opts)
        if ("-d" not in options and "--data" not in options):
            print ("WARNING: No data file specified")
    except:
        print ("SYNTAX:", "<code>.py -d <data destination>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--data"):
            if os.path.isdir(arg):
                datapath = arg
            else:
                print (arg, " is not a directory or does not exist")
                sys.exit(2)
        else:
            assert False, "unhandled option"
    return datapath

def getDataAndKnownPath():
    datapath = ''
    knownpath = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:k:", ["data=", "known="])
        options = list(opt[0] for opt in opts)
        if ("-d" not in options and "--data" not in options):
            print ("WARNING: No data file specified")
        if ("-k" not in options and "--known" not in options):
            print ("WARNING: No known images folder specified")
    except:
        print ("SYNTAX:", "<code>.py -d <data destination> -k <folder containing known faces>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--data"):
            if os.path.isdir(arg):
                datapath = arg
            else:
                print (arg, " is not a directory or does not exist")
                sys.exit(2)
        elif opt in ("-k", "--known"):
            if os.path.isdir(arg):
                knownpath = arg
            else:
                print (arg, " is not a directory or does not exist")
                sys.exit(2)
        else:
            assert False, "unhandled option"
    return [datapath, knownpath]
