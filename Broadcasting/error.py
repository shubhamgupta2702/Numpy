import numpy as np

arr1 = np.array([[1,2,3],[1,2,4]])
arr2 = np.array([2,3])

reshaped = arr1.reshape(2,3)

print(reshaped)


result = reshaped + arr2
print(result)