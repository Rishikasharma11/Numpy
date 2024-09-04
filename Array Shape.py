# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

arr1 = np.array([10,20,30,40], ndmin=4)
print(arr1)
print(arr1.shape)

