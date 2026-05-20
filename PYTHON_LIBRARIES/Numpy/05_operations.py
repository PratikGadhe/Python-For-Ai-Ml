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
print("whole row and column : ",arr[::])
print("Range : ",arr[0:2,0:2])
print("reverse order : ",arr[::-1])

# sorting array
arr = np.array([3,7,2,1,4,9,6,1,0])
print("sorted array : ",np.sort(arr))

# sorting 2d array : 1. by column 2. by row
arr_2d = np.array([[3,1],
                   [4,2],
                   [5,9]])
# 1.Sorting By column (axis = 0) (top to bottom scanning)
print("Sorting by column (top to bottom) : ",np.sort(arr_2d,axis = 0))

# 2.Sorting By row (axis = 1) (left to right scanning)
print("Sorting by row (left to right) : ",np.sort(arr_2d,axis = 1))


# FILTERING THE ARRAY
number = np.array([1,2,3,4,5,6,7,8,9,10])
even = number[1::2] #slicing method
print("By Slicing : ",even)
# numpy allows the expression to be written in []
even_f = number[number%2 == 0]
print("By Filtering : ",even_f)
# filtering by mask 
mask = (number%2 == 0)
e1 = number[mask]
print("filtering by mask : ",e1)

# FANCING INDEXING VS WHERE CLAUSE 
index = [2,4,6]
print("index : ",number[index]) 

where_clause = np.where(number>3)
print("values greater than 3: ",number[where_clause])


# CONDITION ARRAY USING WHERE METHOD 
# syntax : np.where(<condition> , <if true > , <else false> )
condition_array = np.where(number > 3 , "true" , "false")
print(condition_array)