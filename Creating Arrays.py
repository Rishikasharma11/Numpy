# -------------------------------Dimensions in Arrays-----------------------------------------------------
'''A dimension in arrays is one level of array depth (nested arrays).'''

# ------------0-D Arrays----------
'''0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.'''
import numpy as np

arr0 = np.array((20))
print(arr0)

# -----------1-D Arrays-------------
'''An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.'''
arr1 = np.array([10, 20, 30])
print(arr1)

# ------------2-D Arrays------------
'''An array that has 1-D arrays as its elements is called a 2-D array.'''
arr2 = np.array([[10,20,30], [40,50,60]])
print(arr2)

# --------------3-D arrays--------
'''An array that has 2-D arrays (matrices) as its elements is called 3-D array.'''
arr3 = np.array([
    [[1,2,3], [4,5,6]],
    [[6,5,4], [3,2,1]]
    ])
print(arr3)

# ------------------------------------------Number of Dimensions----------------------------------
'''ndim is used to check the number of dimensions'''
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

arr4 = np.array([1,2,3], ndmin = 4)
print(arr4)