# smoothing done when noise is present
import cv2 as cv

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

# blur using the avg of pixel around it , more blur than gaussian for sme kernel size
# Average Blur
avg = cv.blur(img, (7,7))
cv.imshow('avg',avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss',gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('median',median)

#bilatral 
bilateral = cv.bilateralFilter(img, 10, 40, 25)
cv.imshow('bilateral',bilateral)

cv.waitKey(7000)