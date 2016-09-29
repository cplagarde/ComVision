import sys
import cv2
import numpy as np

CV_CAP_PROP_FRAME_COUNT = 7
CV_CAP_PROP_FPS = 5
CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4

img = cv2.imread('Buoys.png')

intrinsic = np.array(
    [[ 299.39646639,    0.,          419.96165812],
     [   0.,          302.5602385,   230.25411049],
     [   0.,            0.,            1.        ]]
)
distortion = np.array(
    [-0.16792771, 0.03121603, 0.00218195, -0.00026904, -0.00263317]
)


edges = cv2.Canny(
	cv2.resize(cv2.split(img)[0], (3 / 4, 3 / 4), 0, 0, cv2.INTER_NEAREST),
    	200, 600, apertureSize=3)
vx, vy, x0, y0 = cv2.fitLine(np.argwhere(edges == 255), 2, 0, 0.01, 0.01)
horizonf.write("%.6f,%.6f,%.6f,%.6f\n" % (vx * 4, vy * 4, x0 * 4, y0 * 4))

writer.write(img)

horizonf.close()
writer.release()








