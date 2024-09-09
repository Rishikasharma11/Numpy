# Random Permutations of Elements
# Shuffling Arrays

from numpy import random
import numpy as np

arr = np.array([3, 8, 2, 7, 4])
random.shuffle(arr)
print("Shuffle:", arr)

# Generating Permutation of Arrays
arr = np.array([1, 2, 3, 4, 5])
print("Permutation:", random.permutation(arr))