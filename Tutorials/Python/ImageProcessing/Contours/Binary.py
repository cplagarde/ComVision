import numpy as np
import cv2

im = cv2.imread('dice.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

