import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# blurring to decrease the contours
canny = cv.Canny(blur, 125, 175) 
# cv.imshow("Canny Edges", canny)

# threshold reads img -> converts to binary -> if px < 125 -> change to black(0) else white(255)
ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

# contours ,hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found using simple canny edges')

contours ,hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found using threshold method')

# drawing contours 
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('contours drawn ',blank)


cv.waitKey(0)