import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# uint8 = dtype of a image
# cv.imshow('Blank',blank)

# 1.paint img a certain color
blank[:] = 0,255,0
print(blank)
cv.imshow('Green',blank)

# 2. draw rectange
# cv.rectangle(blank, (0,0),(250,250), (0,0,255),thickness=5)
cv.rectangle(blank, (0,0),(250,250), (0,0,255),thickness=cv.FILLED)
cv.imshow("Rectange", blank)

# circle/line -> cv.circle/cv.line 

# Put text
cv.putText(blank, "Jigar Pro", (150,250), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), thickness=2)
cv.imshow("text", blank)
cv.waitKey(5000)


