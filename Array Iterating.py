import numpy as np

arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x)
    
arr = np.array([[10, 20, 30],[40, 50, 60]])
for x in arr:
    for y in x:
        print(y)
        
arr = np.array([[[5, 10, 15], [20,25,30]], [[35, 40, 45],[50, 55, 60]]])
for x in arr:
        print(x)
        
for x in arr:
    for y in x:
        for z in y:
            print(z)
            
# Iterating Arrays Using nditer()
arr = np.array([[[0, 2],[4, 6]], [[8, 10], [12, 14]]])
for x in np.nditer(arr):
    print(x)
    
# Iterating Array With Different Data Types
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterating With Different Step Size
for x in np.nditer(arr[:, ::2]):
    print(x)
    
# Enumerated Iteration Using ndenumerate()

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)