# THIS IS IMAGE EDITING OPENCV
from imutils.perspective import four_point_transform
import imutils
import cv2


path = '/home/shohruh/Desktop/start up/wiut/schetchik/'

# 1
# load the example image
image = cv2.imread(path + "saved/wiut-3.jpg")
cv2.imshow("Edged", image)

# pre-process the image by resizing it, converting it to
# grayscale, blurring it, and computing an edge map
# image = imutils.resize(image, height=500)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# edged = cv2.Canny(blurred, 50, 200, 255)
# cv2.imshow("Edged", edged)

#
# cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
# displaCnt = None





# todo
# def detect_gauge():


# print(imutils.__version__)

# import sys
#
#
# print(sys.version_info[0])