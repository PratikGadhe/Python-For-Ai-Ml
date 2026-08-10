import pandas as pd
import numpy as np

df = pd.DataFrame({'roll':[1,2,3,4],'name':['pratik','sanket','tushar','aaditya']})
print(df)
# 1.df.index
print(df.index)

# 2.df.values
print(df.values)

# 3.df.size
print(df.size)

# 4.df.dtype
print(df.dtypes)

# 5.df.T
print(df.T)

# 6.df.axes
print(df.axes)

# 7. df.ndim
print(df.ndim)

# 8.df.shape
print(df.shape)

# 9.df.empty
print(df.empty)