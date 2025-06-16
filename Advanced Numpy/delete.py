'''
np.delete(array, index, axis=none)

return new arrays 
original arrays remains unchanged

'''
import numpy as np

arr = np.array([10,21,31,54,15,181,17])
print(arr)
newArr1 = np.delete(arr, -1)
newArr2 = np.delete(arr, 0)
print(newArr1)
print(newArr2)