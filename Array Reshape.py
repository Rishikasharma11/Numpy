import numpy as np

# Reshape From 1-D to 2-D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("----1-----\n",arr.reshape(2,6))
print("----2-----\n",arr.reshape(3,4))
print("----3-----\n",arr.reshape(4,3))

# Reshape From 2-D to 3-D
print("-----4-----\n",arr.reshape(2,2,3))
print("-----5-----\n",arr.reshape(2,3,2))

# Unknown Dimension
print("-----unknown dimension----\n", arr.reshape(2,2,-1))
print("--------reshape to 1d----\n", arr.reshape(-1))