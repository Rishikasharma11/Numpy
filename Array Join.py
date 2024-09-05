import numpy as np
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([50, 60, 70, 80])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along columns (axis=0):
arr1 = np.array([[10, 20], [30, 40]])
arr2 = np.array([[50, 60], [70, 80]])
arr = np.concatenate((arr1, arr2), axis = 0)
print("\naxis=0\n",arr)

# Join two 2-D arrays along rows (axis=1):
arr = np.concatenate((arr1, arr2), axis = 1)
print("\naxis=1\n", arr)

# Join two 3-D arrays along columns (axis = 0)
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr2 = np.array([[[21, 22, 23], [24, 25, 26]], [[27, 28, 29], [30, 31, 32]]])

newarr1 = np.concatenate((arr1, arr2), axis = 0)
newarr2 = np.concatenate((arr1, arr2), axis = 1)
newarr3 = np.concatenate((arr1, arr2), axis = 2)

print("\n3-D axis=0\n", newarr1)
print("\n3-D axis=1\n", newarr2)
print("\n3-D axis=2\n", newarr3)

# Joining Arrays Using Stack Functions
arr = np.stack((arr1, arr2))
print("\nstack\n", arr)

# hStack - horizontal stack
arr = np.hstack((arr1, arr2))
print("\nhstack\n", arr)

# vStack - verticle stack
arr = np.vstack((arr1, arr2))
print("\nvstack\n", arr)

# Stacking Along Height (depth)
''' NumPy provides a helper function: dstack() to stack along height, which is the same as depth.'''
arr = np.dstack((arr1, arr2))
print("\ndstack\n", arr)