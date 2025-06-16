import numpy as np

arr = np.array([[10,21,31],[87,97,54]])
print(arr)

newArr2D = np.delete(arr, 0, axis=0)
print(newArr2D)