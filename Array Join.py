import numpy as np
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([50, 60, 70, 80])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along columns (axis=0):
arr1 = np.array([[10, 20], [30, 40]])
arr2 = np.array([[50, 60], [70, 80]])
arr = np.concatenate((arr1, arr2), axis = 0)
print("\axis=0\n",arr)

# Join two 2-D arrays along rows (axis=1):
arr = np.concatenate((arr1, arr2), axis = 1)
print("\axis=1\n", arr)

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