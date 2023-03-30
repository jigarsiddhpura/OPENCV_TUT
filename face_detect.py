# FOR ADVANCE FACE DETECTION USE -> DEALINGS FACE RECOGNIZER

import cv2 as cv

img = cv.imread('Resources\Photos\group 1.jpg')
# cv.imshow('lady', img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) 
# faces_rect is the list of coordinates of the face

print(faces_rect)
print(f'No. of faces found = {len(faces_rect)} ')

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)


cv.waitKey(7000)