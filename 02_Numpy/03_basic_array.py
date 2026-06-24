# creating a basic array
import numpy as np
# 1. np.zeros()
arr = np.zeros((2,3))
print(arr)

# 2. np.ones()
arr1 = np.ones((2,3))
print(arr1)

# 3. np.empty()
arr2 = np.empty((2,3))
print(arr2)

# 4.np.arange(4)
arr3 = np.arange(2,11,2)
print(arr3)

# 5.np.linspace(0,10,num=5)
arr4 = np.linspace(0,10,num=7)
print(arr4)

# 6. specific datatype
arr5 = np.zeros((2,3),dtype = int)
print(arr5)