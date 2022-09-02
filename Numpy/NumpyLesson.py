#matlab replacement
#useful in machine learning

import numpy as np

a = np.array([1,2,3])
print(a)

#get dimension
a.ndim
#get shape
a.shape
#get item type
a.dtype
#get item itemsize
a.itemsize

#acessing items and slicing is used just like normal arrays/lists

#matrix initiation
#use np.zeros or np.ones
#use .copy function when copying arrays
#You can use arrays as an index in order to access items