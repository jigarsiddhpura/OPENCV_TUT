import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('parm', img)

# translate
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]]) #????????????
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,100,-100)
# cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img , rotMat, (width,height))
    
rotated = rotate(img,-45)
# cv.imshow('rotated', rotated)

# flip
# 0 - vertical flip, 1 - horizontal flip , -1 - both
flipped = cv.flip(img,-1)
cv.imshow('flipped', flipped)



    


cv.waitKey(7000)
