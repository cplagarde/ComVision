# import shit
import cv2
import numpy as np

img = cv2.imread('histogram4.jpg', 0)

# create a CLAHE object (Arguements are optional).
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize= (8,8))
cl1 = clahe.apply(img)

res = np.hstack((img, cl1)) #stacking images side-by-side

cv2.imwrite('res2.jpg', res)


cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows

