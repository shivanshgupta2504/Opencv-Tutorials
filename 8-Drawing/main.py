import cv2

# Here we can draw some basic lines and polygons on an image

img = cv2.imread('whiteboard.png')

# print(img.shape) # (height, width, color channels)

# Lines
cv2.line(img, (0,0), (100, 100), (155, 155, 155), 3) # updates original image

# Rectangle
cv2.rectangle(img, (200, 200), (400, 400), (0, 255, 0), -1)
# giving thichness = -1 gives a filled rectangle

# Circle
cv2.circle(img, (600, 400), 100, (255, 0, 0), 3)

# Text
cv2.putText(img, "Hello world", (550, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)

# These drawings are permanent changes to the image

cv2.imshow("Whiteboard", img)
cv2.waitKey(0)