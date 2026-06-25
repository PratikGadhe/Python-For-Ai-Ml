# creating array from scratch using different build in methods 
import numpy as np

# 1. sorting an array using np.sort(arr)
arr = np.array([3,7,2,1,4,9,6,1,0])
print("sorted array : ",np.sort(arr))

# sorting 2d array : 1. by column 2. by row
arr_2d = np.array([[3,1],
                   [4,2],
                   [5,9]])
# a.Sorting By column (axis = 0) (top to bottom scanning)
print("Sorting by column (top to bottom) : ",np.sort(arr_2d,axis = 0))

# b.Sorting By row (axis = 1) (left to right scanning)
print("Sorting by row (left to right) : ",np.sort(arr_2d,axis = 1))

# 2. Concetenate two array using np.concatenate((arr1,arr2))
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
merge = np.concatenate((arr1,arr2))
print("Merging arrays : ",merge)

# 3. merging two different dimensions array vertically
arr1 = np.array([1,2,3])
arr2 = np.array([[4,5,6]
                 ,[7,8,9]])
merge = np.vstack((arr1,arr2))
print(merge)

# 3. merging two different dimensions array vertically
arr1 = np.array([1,2,3],[7,7,7])
arr2 = np.array([[4,5,6]
                 ,[7,8,9]])
merge = np.hstack((arr1,arr2))
print(merge)

# 7. finding index of array using np.where(<condition>)
where = np.where(arr > 3)
print("index : ",where)
print("values greater than 3 : ",arr[where])
print("values greater than 3 (sort): ",np.sort(arr[where]))


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

#11. removing elements using np.delete(<arr>,<slicing/indexing>)
arr = np.array([1,2,3,4,5,6])
delete = np.delete(arr,2)
print(delete)

# 12. adding columns / rows using np.sum(<arr> , axis)
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000]
])
sum_column = np.sum(sales_data[:,1:],axis = 0)
print(sum_column)
sum_row = np.sum(sales_data[:,1:],axis = 1)
print(sum_row)

#13. minimum by column and row 
print("column : ",np.min(sales_data[:,1:],axis = 0))
print("row : ",np.min(sales_data[:,1:],axis = 1))

#14. maximum by column and row 
print("column : ",np.max(sales_data[:,1:],axis = 0))
print("row : ",np.max(sales_data[:,1:],axis = 1))

#15. average by column and row 
print("column : ",np.mean(sales_data[:,1:],axis = 0))
print("row : ",np.mean(sales_data[:,1:],axis = 1))
