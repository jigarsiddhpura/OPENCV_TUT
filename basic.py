import cv2 as cv

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('park', img)

# grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayye', gray)

# blurring
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blurred', blur)

# ⭐ edge cascade
canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175) 
cv.imshow('Canny Edges',canny)

# Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries.

# dilate
dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow('dilated', dilated)

#erode 
erroded = cv.erode(dilated,(7,7), iterations=3)
# cv.imshow('erroded', erroded)

#resize
resized = cv.resize(img,(1000,800), interpolation=cv.INTER_CUBIC)
# resizedL = cv.resize(img,(1000,800), interpolation=cv.INTER_LINEAR)
# cv.imshow('resized', resized)

#cropping
cropped = img[100:200,200:400]
# cv.imshow('cropped', cropped)


cv.waitKey(6000)