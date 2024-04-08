import cv2 as cv

# read the webcam
webcam = cv.VideoCapture(0)

# Visualize from webcam
while True:
    ret, frame = webcam.read()

    cv.imshow('Webcam', frame)
    # To break out of while loop
    if cv.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()