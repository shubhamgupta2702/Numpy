'''
convert multidimensional array into a one d array or a line.
.ravel() -> view
.flatten() -> copy
'''

import numpy as np

arr = np.array([[10,40,10],[1,2,3]])

print(arr.ravel())
print(arr.flatten())