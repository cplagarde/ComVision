# import shit
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "undefined"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# Triangle
		if len(approx) == 3:
			shape = "triangle"

		# Square or rectangle
		elif len(approx) == 4:
			# compute the bounding box of contour 
			# and use it to compute aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have equal aspect ratio
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		# Pentagon
		elif len(approx) == 5:
			shape = "pentagon"

		# assume circle
		else:
			shape = "circle"

		# return shape name
		return shape
