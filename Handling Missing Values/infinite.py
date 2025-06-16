#np.isinf() 10**1000
#1/0

import numpy as np

arr = np.array([[1,2,3,4,np.inf],[40,np.inf, -np.inf, 90, np.inf]])

print(np.isinf(arr))