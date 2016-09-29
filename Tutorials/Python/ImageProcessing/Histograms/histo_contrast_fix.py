import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('histogram2.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ)) #stacking images side-by-side
cv2.imwrite('res.png', res)

imgF = cv2.imread('res.png')
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows


