import cv2
import numpy as np
import argparse


cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([0,50,50],dtype=np.uint8)
    upper_red = np.array([20,255,255],dtype=np.uint8)
    lower_green = np.array([50,50,50],dtype=np.uint8)
    upper_green = np.array([70,255,255],dtype=np.uint8)
    lower_blue = np.array([110,50,50],dtype=np.uint8)
    upper_blue = np.array([130,255,255],dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    maskG = cv2.inRange(hsv, lower_green, upper_green)
    maskB = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('maskR',maskR)
    cv2.imshow('maskG',maskG)
    cv2.imshow('maskB',maskB)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()