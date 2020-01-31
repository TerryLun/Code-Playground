import cv2
import numpy

img = cv2.imread('smallgray.png', 0)
cv2.imwrite('img_copy.png', img)
