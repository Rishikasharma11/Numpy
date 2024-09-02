import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

# Adding elements using index number
print(arr[2] + arr[3])

# Access 2-D Arrays
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("The 3rd element of 1st array is:", arr[0, 2])
print("The 4th element of 2nd array is:", arr[1, 3])

# Access 3-D Arrays
arr = np.array([[[10, 20, 30, 40], [50, 60, 70, 80]], [[90, 100, 110, 120], [130, 140, 150, 160]]])
print(arr[0, 0, 2])
print(arr[1, 0, 2])

# ------------Negative Indexing---------------
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Last  element from 2nd dim", arr[1, -1])