import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([180,50,50])
    upper_blue = np.array([260,255,255])
    # define range of red color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([20,255,255])
    # define range of green color in HSV
    lower_green = np.array([30,50,50])
    upper_green = np.array([150,255,255])

    # Threshold the HSV image to get only blue, red, and green colors
    maskB = cv2.inRange(hsv, lower_blue, upper_blue)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    maskG = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    resB = cv2.bitwise_and(frame,frame, mask= maskB)
    resR = cv2.bitwise_and(frame,frame, mask= maskR)
    resG = cv2.bitwise_and(frame,frame, mask= maskG)

    cv2.imshow('maskB',maskB)
    cv2.imshow('maskG',maskG)
    cv2.imshow('maskR',maskR)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()