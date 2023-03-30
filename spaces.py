import cv2 as cv
import matplotlib.pyplot as plt
# reading pics

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('park', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)


rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# matplotlib reads img as RGB while opencv as BGR ⭐
plt.imshow(rgb)
plt.show()


cv.waitKey(7000)