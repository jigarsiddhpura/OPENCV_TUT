import cv2 as cv

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# simple threshold

# threshold , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)

threshold , thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh inverse',thresh_inv)

# Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(10000)