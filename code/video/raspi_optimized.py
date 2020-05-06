import numpy as np
import cv2
import time
from PIL import Image
from face_functions import *

# MODEL = "hog"

datapath = getDataPath()

vid = cv2.VideoCapture(0)
time.sleep(2.0)

while (True):
    ret, img = vid.read()
    image = Image.fromarray(img)
    image.thumbnail((700,700))
    image = np.asarray(image)

    locations = detectFace(image)
    recognizeFace(image, locations, datapath)

    cv2.imshow ('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
