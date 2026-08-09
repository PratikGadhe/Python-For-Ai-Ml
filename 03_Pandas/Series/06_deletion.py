# we can use drop() to delete the elements from series
import pandas as pd
import numpy as np

s1 = pd.Series([1,2,4,4,5,np.nan])
print(s1.drop(2))
print(s1)

# we can also delete the multiple values
print(s1.drop([1,3]))
print(s1)

# to delete nan value 
print(s1.dropna())
print(s1)

# to delete the duplicate value
print(s1.drop_duplicates())