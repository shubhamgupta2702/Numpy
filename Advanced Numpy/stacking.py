"""
vertically
horizontally

vstack() row wise
hstack() column wise
"""


import numpy as np

arr = np.array([1,5,4])
arr2 = np.array([14,54,7])

print(np.vstack((arr2, arr))) #vertically stack
print(np.hstack((arr, arr2)))  #horizonally stack
