import cv2
import numpy as np

img = cv2.imread('smallgray.png', 1)
cv2.imwrite('img_copy.png', img)

arr = np.zeros((10, 10), dtype=int)
print(arr)

arr2 = np.vstack((img, img))
print(img)
print(arr2)
