'''
reshape(rows, columns) specify new shape
if dimensions match
'''

import numpy as np

arr = np.array([10,40,10,42,32,87])

reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)