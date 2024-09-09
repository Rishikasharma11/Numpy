# Generate Random Number
from numpy import random
x = random.randint(100)
print(x)

# Generate Random Float
x = random.rand()
print(x)

# Generate Random Array
x = random.randint(100, size=5)
print(x)

# 2-D array
x = random.randint(100, size=(2, 3))
print(x)

x = random.rand(5)
print(x)

# 2-D array
x = random.rand(2,3)
print(x)

# Generate Random Number From Array
x = random.choice([2, 4, 8, 11, 14])
print(x)

x = random.choice([1, 2, 3, 4, 5], size = (2,5))
print(x)