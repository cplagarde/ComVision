import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('star2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = M['m00']


print M
print cx
print cy
print area


plt.subplot(321),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(gray,cmap = 'gray')
plt.title('ret'), plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(blurred,cmap = 'gray')
plt.title('thresh'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(thresh,cmap = 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])
# plt.subplot(325),plt.imshow(contours,cmap = 'gray')
# plt.title('hierarchy'), plt.xticks([]), plt.yticks([])
plt.show()


