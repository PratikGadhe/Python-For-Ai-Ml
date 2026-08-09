import pandas as pd
import numpy as np

# methods to create a Series
# syntax : pd.Series(<methods>)
# 1. Empty Series 
s1 = pd.Series()
print(s1)

# 2. list method
s2 = pd.Series([1,2,3,4])
print(s2)

# series using two list 
l1 = [1,2,3]
l2 = ['a','b','c']
s3 = pd.Series(l1,l2)   #bydefault : l1 = data , l2 = index
print(s3)

# 3. series using range method 
s4 = pd.Series(range(10))
print(s4)
# for indexing of range we will use comprehensive for loop
s4 = pd.Series(range(10),index = [x for x in range(10)])
print(s4)

"""
Note : 
1. type casting 
s1 = pd.Series([1,2,0.5])
this will convert whole series into float
output >>> dtype : float64

2. missing value : to store missing value in series
s2 = pd.Series([1,2,np.NaN])
>>> 0   1
    1   2
    2   NaN
"""
# 4. Scaler value / constant value
s1 = pd.Series(62,index = ['p','r','a','t','i','k'])
print(s1)

# 5.Mathematical expression
ind = np.arange(10)
data = ind**2
s2 = pd.Series(data,index = ind)
print(s2)

# 6. using numpy array
np_arr = np.array([10,20,30,40])
s1 = pd.Series(np_arr)
print(s1)

# 7. using dictionary
dict = {'a':1,'b':2,'c':3,'d':4}
s1 = pd.Series(dict)
print(s1)