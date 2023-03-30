import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    # for live video, videos, images
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimensions = (width,height)
    # to shrink -> INTER_AREA , to enlarge -> INTER_CUBIC / INTER_LINEAR ⭐
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # only for live videos
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Resources\Videos\dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     resized_frame = rescaleFrame(frame)

#     cv.imshow('Video', frame)
#     cv.imshow('Resized Video', resized_frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow('CatL', img)
resized_img = rescaleFrame(img)
cv.imshow('Cat resized', resized_img)
cv.waitKey(5000)
