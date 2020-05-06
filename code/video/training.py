from face_functions import *

datapath, knownpath = getDataAndKnownPath()

print ("Loading known faces...")
trainModelOptimized(knownpath, datapath)
