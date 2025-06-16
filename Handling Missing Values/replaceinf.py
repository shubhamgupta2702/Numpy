import numpy as np

arr = np.array([[1,2,3,4,np.inf],[40,np.inf, -np.inf, 90, np.inf]])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-786)

print(cleaned_arr)
