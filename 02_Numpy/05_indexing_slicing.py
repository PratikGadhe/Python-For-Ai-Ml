# indexing and slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])

# slicing
print("basic slicing : ",arr[2:7])
print("step slicing : ",arr[1:8:2])
print("negative slicing : ",arr[-3])
print("reverse slicing : ",arr[::-1])

# accessing elements from 2d array
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print("Single element : ",arr[1,1])
print("single row : ",arr[1])
print("single column : ",arr[:,1])
print("whole row and column : ",arr[:,:])
print("Range : ",arr[0:2,0:2])
print("reverse order : ",arr[::-1])

# examples 
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# 1.print all of the values in the array that are less than 5.
print(a[a<5])
# 2. select elements that are divisible by 2:
div = (a%2==0)
print(a[div])
# 3. select the element greater than 2 and less than 11
c = a[(a > 2) & (a < 11)]
print(c)

# note : special method called np.nonzero() can also be use to select/access the values
b = np.nonzero(a<5)
print(b)
