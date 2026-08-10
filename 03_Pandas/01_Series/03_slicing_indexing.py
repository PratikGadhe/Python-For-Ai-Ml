# accessing the elements using slicing/indexing
import pandas as pd
import numpy as np
s1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s1)
# syntax : <var_name>[<start>:<stop>:<step>]
print(s1[:]) # all elements
print(s1[:3]) #top 3 elements
print(s1[-3:]) #last 3 elements
print(s1[::-1]) #reverse elements

# methods to. access elements
# 1. iloc[<start>:<stop>]
print(s1.iloc[:]) # all elements
print(s1.iloc[:3]) #top 3 elements
print(s1.iloc[-3:]) #last 3 elements
print(s1.iloc[::-1])

# 2.loc[<index_name> range]
print(s1.loc['a':'e'])
print(s1.loc[:'c']) #top 3 elements
print(s1.loc['c':]) #last 3 elements
print(s1.loc[::-1])