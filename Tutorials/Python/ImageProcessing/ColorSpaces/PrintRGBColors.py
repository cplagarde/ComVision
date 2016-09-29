import cv2
import numpy as np

green = np.uint8([[[0,255,0]]])
blue = np.uint8([[[255,0,0]]])
red = np.uint8([[[0,0,255]]])

hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

print hsv_red
print hsv_green
print hsv_blue

