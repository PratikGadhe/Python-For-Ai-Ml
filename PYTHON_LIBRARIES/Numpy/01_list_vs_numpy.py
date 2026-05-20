import time
import numpy as np
arr_1d = np.array([1,2,3,4])
print(arr_1d)

arr_2d = np.array([[2,3,4],[4,5,6]])
print(arr_2d)

# list multiplication 
py_list = [1,2,3]
print(py_list*2)

# array multiplication 
py_array = np.array([1,2,3])
print(py_array*2)

# time efficiency
start = time.time()
py_list = [i*2 for i in range(10000000)]

print("\n List operation time:", time.time() - start)
start = time.time()
p_array = np.arange(10000000) * 2
print("\n Numpy operation time:",time.time()- start)

# creating array in numpy from scratch 
# 1. zeroes (used to fill array with zeros)
zero = np.zeros((3,3))
print(zero)

# 2. ones (used to fill array with ones)
ones = np.ones((2,2))
print(ones)

# 3. full (used to fill the array with constant value)
full = np.full((3,3),63)
print(full)

# 4. arange used to create array by giving a range 
r = np.arange(0,11,2)
print(r)

rand = np.random.random((2,3))
print(rand)