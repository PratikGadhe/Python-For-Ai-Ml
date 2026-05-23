# ADDING AND REMOVING ELEMENTS FROM ARRAY
# 1. merge two array
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
add = arr1 + arr2 
print(add)
# merge
merge = np.concatenate((arr1,arr2))
print(merge)

# 2. adding row in 2d array
original = np.array([[1,2],[3,4]])
new_row = np.array([5,6])
with_row = np.vstack((original,new_row))
print(with_row)

# 3. adding new column in 2d array
original = np.array([[1,2],[3,4]])
new_column = np.array([[7],[8]])
with_column = np.hstack((original,new_column))
print(with_column)

# removing elements 
arr = np.array([1,2,3,4,5,6])
delete = np.delete(arr,2)
print(delete)

# removing element from 2d array
arr_2d = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,8,7,6]])
delete = np.delete((arr_2d,[1,2]))
print(delete)