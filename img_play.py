import cv2
import numpy as np

img = cv2.imread('smallgray.png', 0)
cv2.imwrite('img_copy.png', img)

arr = np.zeros((2,3))

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)