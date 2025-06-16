#np.nan_to_num(array, nan=value)  default - 0

import numpy as np

arr = np.array([2,3,np.nan, 54, np.nan])
cleaned_arr = np.nan_to_num(arr)

cleaned_arr1 = np.nan_to_num(arr, nan=10)

print(cleaned_arr)
print(cleaned_arr1)