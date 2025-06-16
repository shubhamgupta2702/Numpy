import numpy as np

arr = np.array([1,2,np.nan, 5,5, np.nan])

print(np.isnan(arr))


#not we cannot compare it directly.
print(np.nan == np.nan)