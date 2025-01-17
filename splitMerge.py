import cv2 as cv
import numpy as np


img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
# cv.imshow('merged',merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# light shade high density & vice versa
# cv.imshow("red",r)
# cv.imshow("blue",g)
# cv.imshow("green",b)

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)


cv.waitKey(7000)