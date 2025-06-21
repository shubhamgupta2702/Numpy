import numpy as np

arr = np.array([2,1,3,4,50])

print(arr[:-1]) #[2 1 3 4]
print(arr[-1]) #50

print(arr[::]) #[ 2  1  3  4 50]

print(arr[::-1]) #[50  4  3  1  2]  -> reverse

print(arr[::-2]) #[50  3  2]