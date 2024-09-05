import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[2:6])

# Negative Slicing
print(arr[-4 :-1])

# STEP
print(arr[1:5:2])

# Return every other element from the entire array:
print(arr[::2])

# Slicing 2-D Arrays
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4])
