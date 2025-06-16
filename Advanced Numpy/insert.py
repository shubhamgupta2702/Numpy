"""
np.insert(array, indexno, value, axis=none)
array- original array
index -
value -
axis = 0, row-wise
axis=1, column wise
axis=none, flattened version- (single line)

"""
import numpy as np

arr = np.array([10,40,10,42,32,87])
new_arr = np.insert(arr, 3, 69, axis=0)
print(arr)
print(new_arr)