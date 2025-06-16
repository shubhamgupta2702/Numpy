'''
np.concatenate((array1, array2), axis = 0)

axis 0 -> vertical stacking
axis 1 -> horizontal stacking
'''

import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([90,80,70])

newArr = np.concatenate((arr1, arr2))
print(newArr)