import numpy as np

list1 = [10,20,30,40]
list2 = [2,1,4,5]
list3 = [8,7,9,3]

arr = np.array([list1,list2,list3])
print(arr)


print(arr.shape) #(rows, columns)

list1[2] = 999 # indexing

print(list1)