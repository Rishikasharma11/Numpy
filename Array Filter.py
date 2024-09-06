import numpy as np

arr = np.array([10, 20, 30, 40, 50])
x = np.array([True, False, True, True, False])
print(arr[x])

arr = np.array([100, 200, 300, 400, 500])
filter_arr = []
for x in arr:
    if x > 300:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


arr = np.array([100, 200, 300, 400, 500])
filter_arr = []
for x in arr:
    if x % 3 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)