import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# mask = cv.bitwise_and(gray,gray, mask=circle)
masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked',masked)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.xlabel('Bins (Pixel Intensity)')
plt.ylabel('# of pixels')
# plt.title('Grayscale histogram')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram

plt.title('Color histogram')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(7000)