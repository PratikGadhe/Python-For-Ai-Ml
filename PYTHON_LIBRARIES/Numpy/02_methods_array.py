# creating array from scratch using different build in methods 
import numpy as np

# 1. zeroes array 
zero = np.zeros((3,4))
print(zero)

# 2. ones array 
one = np.ones((2,3))
print(one)

# 3. constant array using full()
constant_value = np.full((3,3),63)
print(constant_value)

# 4. array with random value using random class
random = np.random.random((3,3))
print(random)
# remember .random is class having lots of methods in it

# 5. creating squence array using arange() method
sequence = np.arange(0,11,2)
print(sequence)

# 6. sorting an array using np.sort(arr)
arr = np.array([3,7,2,1,4,9,6,1,0])
print("sorted array : ",np.sort(arr))

# 7. finding index of array using np.where(<condition>)
where = np.where(arr > 3)
print("index : ",where)
print("values greater than 3 : ",arr[where])
print("values greater than 3 (sort): ",np.sort(arr[where]))

# 8. Concetenate two array using np.concatenate((arr1,arr2))
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
merge = np.concatenate((arr1,arr2))
print("Merging arrays : ",merge)

# 9. adding row in 2d array
original = np.array([[1,2],[3,4]])
new_row = np.array([5,6])
with_row = np.vstack((original,new_row))
print(with_row)

# 10. adding new column in 2d array
original = np.array([[1,2],[3,4]])
new_column = np.array([[7],[8]])
with_column = np.hstack((original,new_column))
print(with_column)