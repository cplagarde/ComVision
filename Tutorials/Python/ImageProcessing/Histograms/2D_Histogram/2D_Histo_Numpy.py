# import shit
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('house.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

