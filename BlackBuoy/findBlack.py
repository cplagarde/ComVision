# Not much different than the original code. It has some issues with some .jpg files since the compression method it uses. I suggest using a .png to avoid any issues.
# http://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

# import shit
import argparse
import imutils
import cv2

# construct the arguement parse and parse the arguement
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# loop over the contours
for c in cnts:	
	# compute the center of the contour
	M = cv2.moments(c)
	if M["m00"] > 0:
		x = int(M["m10"] / M["m00"])
		y = int(M["m01"] / M["m00"])

# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]


# M = cv2.moments(thresh, 0)
# area = M['m00']
# if(area > 1500): 
# 	#determine the x and y coordinates of the center of the object 
#     #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
#     x = M['m10'] / area
#     y = M['m01'] / area

# draw the contour and center of the shape on the image
cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
cv2.circle(image, (x, y), 7, (255, 255, 255), -1)
cv2.putText(image, "center", (x - 20, y - 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# show the image
cv2.imshow("Image", image)
cv2.waitKey(0)


cv2.imwrite('BlackBuoy.png', image)