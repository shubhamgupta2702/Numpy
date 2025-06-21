import numpy as np

lst1 = [2,5,4,8]
lst2 = [8,7,9,5]
lst3 = [0,2,4,3]

nparr = np.array([4,5,1,8])
arr = np.array([lst1, lst2, lst3])

print(arr)
print("operations \n")

print(arr[:,1])
# print(arr[1:1])
print(arr[1:,1:3])

print(arr[1:,2:3])

print(arr[0::4])

print(nparr <3)

print(nparr[nparr >2])

print(arr.reshape(4,3))

