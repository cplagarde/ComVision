# import shit
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('histogram1.jpg', 0)

# Native OpenCV histogram calculation (40X speed than np.histogram)
hist = cv2.calcHist([img], [0], None, [256], [0,256])

# # Numpy histogram function
# hist, bin = np.histogram(img.ravel(),256,[0,256])

# # 10X speed than np.histogram
# hist = np.bincount(img.ravel(), minlength = 256)

plt.hist(img.ravel(), 256, [0,256])
plt.show()

