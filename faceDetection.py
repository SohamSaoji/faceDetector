# code for face detection using opencv in python

# pip install opencv
import cv2

# Load the Cascade
face_cascade = cv2.CascadeClassifire('haarcascade_frontalface_defalt.xml')

# Read the input image
img = cv2.imread('image.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
faces = face_cascade.detectMultiScale(gray, 1.1,4)

# Draw rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h), (255,0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waiteKey()