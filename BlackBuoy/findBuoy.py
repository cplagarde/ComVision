# import shit
import numpy as np
import cv2
import imutils
from matplotlib import pyplot as plt

image = cv2.imread('OneBBuoy.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

Track_MIN = np.array([0, 0, 0],np.uint8)
Track_MAX = np.array([180, 255, 100],np.uint8)
thresh2= cv2.inRange(hsv_img, Track_MIN, Track_MAX)
thresh3 = thresh2
thresh3[0:75,0:720] = 0
thresh3[0:480,650:720] = 0

plt.subplot(321),plt.imshow(image,cmap = 'gray')
plt.title('image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(gray,cmap = 'gray')
plt.title('gray'), plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(hsv_img,cmap = 'gray')
plt.title('hsv'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(thresh,cmap = 'gray')
plt.title('thresh'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(thresh2,cmap = 'gray')
plt.title('thresh2'), plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(thresh3,cmap = 'gray')
plt.title('thresh3'), plt.xticks([]), plt.yticks([])
plt.show()

