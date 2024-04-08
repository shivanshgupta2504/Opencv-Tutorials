import cv2

# Reading the image
img = cv2.imread('birds.jpg')

# Write/Store the image
cv2.imwrite('birds_out.jpg', img)

# Visualize the image
cv2.imshow('Image', img)
cv2.waitKey(0)