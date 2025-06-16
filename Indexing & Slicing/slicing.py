"""
slicing

array[start:stop:step]

arr[start:end] , start to end -1
negative step can also pass
"""

import numpy as np

arr = np.array([10,40,10,42,32,87])
print(arr[1:5])
print(arr[2:4:2])
print(arr[::2]) #every second element
print(arr[::-1])  # reverse 