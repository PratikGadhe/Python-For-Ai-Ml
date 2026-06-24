# Numpy Foundation and creation of numpy 
import numpy as np
import time as t
arr_1d = np.array([1,2,3])
print(type(arr_1d))

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

# list vs numpy array

py_list = [1,2,3]
print("multiplication : ",py_list * 2)

np_array = np.array([1,2,3])
print("multiplication : ",np_array * 2)

# why to use numpy ? 
start = t.time()
py_list = [i*2 for i in range(100000)]
print("list operation time : ",t.time()-start)

start = t.time()
np_array = np.arange(100000) * 2
print("numpy operation time : ",t.time()-start)
# output : 
# list operation time :  0.007361650466918945
# numpy operation time :  0.0032362937927246094