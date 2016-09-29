# import shit
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('histogram3.jpg', 0)
hist, bin = np.histogram(img.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf', 'historgram'), loc = 'upper left')
plt.show()

# img = cv2.imread('histogram2.jpg')
# cv2.imshow('image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255/ (cdf_m.max() - cdf_m.min())
cdf_m = np.ma.filled(cdf_m, 0).astype('uint8')

# img2 = cdf[img]
# img = img2


# hist, bin = np.histogram(img.flatten(), 256, [0,256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()

# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(), 256, [0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf', 'historgram'), loc = 'upper left')
# plt.show()

# cv2.imshow('image', img)

