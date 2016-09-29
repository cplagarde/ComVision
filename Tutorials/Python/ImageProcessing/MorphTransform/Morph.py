import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(331),plt.imshow(img),plt.title('Normal')
plt.subplot(332),plt.imshow(erosion),plt.title('erosion')
plt.subplot(333),plt.imshow(dilation),plt.title('dilation')
plt.subplot(334),plt.imshow(opening),plt.title('opening')
plt.subplot(335),plt.imshow(closing),plt.title('closing')
plt.subplot(336),plt.imshow(gradient),plt.title('gradient')
plt.subplot(337),plt.imshow(tophat),plt.title('tophat')
plt.subplot(338),plt.imshow(blackhat),plt.title('blackhat')
plt.show()
