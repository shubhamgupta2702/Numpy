import numpy as np

arr = np.array([1,2,3,4,5.3])
int_arr = arr.astype(int)

print(int_arr)
print(arr.dtype)

#after conversion
print(int_arr.dtype)