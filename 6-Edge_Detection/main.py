import cv2
import numpy as np

img = cv2.imread('basketball-player.jpg')

img_edge = cv2.Canny(img, 100, 150) 
# these two numbers are first and second threshold for hysteresis procedure
# use trial and error for the desired results

#Dilation
img_dilate = cv2.dilate(img, np.ones((50, 50), dtype=np.int8))
img_edge_dilate = cv2.dilate(img_edge, np.ones((10,10), dtype=np.int8))

#Erosion
img_erode = cv2.erode(img, np.ones((10, 10), dtype=np.int8))
img_dilate_erode = cv2.erode(img_edge_dilate, np.ones((10, 10), dtype=np.int8))

cv2.imshow('Image', img)
# cv2.imshow('Dilate Image', img_dilate)
# cv2.imshow('Eroded Image', img_erode)
cv2.imshow('Edge Image', img_edge)
cv2.imshow('Dilate Edge Image', img_edge_dilate)
cv2.imshow('Dilated-Eroded Image', img_dilate_erode)

cv2.waitKey(0)