import cv2

img = cv2.imread('birds.jpg')

# Change to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Do thresholding - use Binary inverse thresholding
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(thresh, cnt, -1, (0, 255, 0), 2)
        x1, y1, w, h = cv2.boundingRect(cnt)
        
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + w), (0, 255, 0), 2)

cv2.imshow("Img", img)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)