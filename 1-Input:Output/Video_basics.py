import cv2 as cv

# read video
video = cv.VideoCapture('sample_video.mp4')

# visualize the video
ret = True

while ret:
    ret, frame = video.read()
    # ret is a boolean value indicating a frame is successfully read or not
    if ret:
        cv.imshow('Frames', frame)
        cv.waitKey(40)

video.release()  # deallocate the memory occupied by video
cv.destroyAllWindows()
