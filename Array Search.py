'''You can search an array for a certain value, and return the indexes that get a match.
To search an array, use the where() method.'''
import numpy as np
arr = np.array([2, 4, 6, 8, 10])
newarr = np.where(arr == 6)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
newarr = np.where(arr == 4)
print(newarr)

# Find the indexes where the values are even:
arr = np.array([10, 20, 30, 40, 50])
newarr = np.where(arr % 2 == 0)
print(newarr)

# Find the indexes where the values are odd:
newarr = np.where(arr % 2 == 1)
print(newarr)

# Searchsorted- gives index
arr = np.array([1, 4, 7, 8])
newarr = np.searchsorted(arr, 7)
print(newarr)

# Search From the Right Side
arr = np.array([1, 4, 7, 8])
newarr = np.searchsorted(arr, 4, 'right')
print(newarr)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

arr = np.array([10, 20, 30, 40 , 50])
x = np.searchsorted(arr, [5, 15, 25])
print(x)

# linespace- will break in from 2 to 16 in 3 parts
newarr = np.linspace(2,16,3)
print(newarr)