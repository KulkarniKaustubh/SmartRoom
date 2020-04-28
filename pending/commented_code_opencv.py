# this is all commented out code

# image = cv2.imread(f"{KNOWN_FACES_DIR}/{name}/{file}{new}")
# image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# locations = fr.face_locations(image, model=MODEL)
# locations = face_cascade.detectMultiScale(image, 1.5, 5)
# print (locations)
# loc3 = []
# for (x, y, w, h) in locations:
    # loc3.append((y, x+w, y+h, x))
    # loc3.append((x, y, x+w, y+h))
    # cv2.rectangle(image,(y, x+w),(y+h, x),(255,0,0),2)

# print (loc3)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('temp', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# locations2 = fr.face_locations(image, model=MODEL)
# print (locations2)
# break


# top_left = (face_location[0], face_location[1])
# bottom_right = (face_location[2], face_location[3])
