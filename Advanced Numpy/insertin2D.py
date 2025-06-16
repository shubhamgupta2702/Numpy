import numpy as np

arr = np.array([[10,40,10],[42,32,87]])

# insert a new row at index 1
new_arr = np.insert(arr, 0, [3,2,1], axis=0)
print(new_arr)