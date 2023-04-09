import os
import cv2 as cv
import numpy as np

DIR = r'D:\OPENCV_TUT\Resources\Faces\train'
people = []

for i in os.listdir(DIR):
    people.append(i)

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

img = cv.imread(r"D:\OPENCV_TUT\Resources\Faces\val\ben_afflek\2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detect face
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Predicted {people[label]} with confidence {confidence}')

    cv.putText(img, people[label], (10,30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h),  (0,255,0), thickness=2)

cv.imshow("detected", img)
cv.waitKey(3000)