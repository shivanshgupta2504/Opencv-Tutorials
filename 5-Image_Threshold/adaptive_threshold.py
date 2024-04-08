import cv2

img = cv2.imread('handwritten.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY) # not working

# Adaptive thresholding
adptvThresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('Image', img)
cv2.imshow('Threshold Image', thresh)
cv2.imshow('Adaptive Threshold Image', adptvThresh)
cv2.waitKey(0)