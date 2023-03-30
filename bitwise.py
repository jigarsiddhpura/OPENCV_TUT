import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros((400,400) ,dtype='uint8')

rectange = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle',rectange)
cv.imshow('circle',circle)

bitwise_and = cv.bitwise_and(rectange,circle)
cv.imshow('bAND', bitwise_and)

bitwise_xor = cv.bitwise_xor(rectange,circle)
cv.imshow('bXOR', bitwise_xor)

#similar w OR

bitwise_not = cv.bitwise_not(rectange)
cv.imshow('bNOT', bitwise_not)



cv.waitKey(0)