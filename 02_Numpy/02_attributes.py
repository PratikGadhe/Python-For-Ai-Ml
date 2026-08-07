# Properties of numpy array 
import numpy as np 
array = np.array([[1,2,3],
                  [4,5,6]])
# 1. size
print("Size : ",array.size)
# 2. type
print("Data type : ",array.dtype)
# 3. shape
print("Shape : ",array.shape)
# 4. dimension
print("dimension : ",array.ndim)
# 5. Transpose
print("transpose : ",array.T)
# 6. reshaping the array 
arr = np.arange(12)
# converting 1d array into 2d using .reshape() method
reshaped = arr.reshape((3,4))
print("Reshaped array : \n",reshaped)
print("original array : ",arr)
print(reshaped.ndim)

# 7. arr.flatten((row,columns))
# converting nested array into 1 dimension
arr = np.array([[1,2,3],[4,5,6]])
print("original array : \n",arr)
flatten = arr.flatten()
print("flatten array : ",flatten)