# The sun of the probabilty will not be more than to 1. 
# The one with higher probability will be printed
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)