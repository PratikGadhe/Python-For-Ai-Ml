import pandas as pd
import numpy as np
# attributes in series:
# 1. s1.index
s1 = pd.Series([1,2,3,np.nan,5],index = ['a','b','c','d','e'])
print(s1.index)

# 2. s1.values
print(s1.values)

# 3. s1.size
print(s1.size)

# 4. s1.hasnans
print(s1.hasnans)

# 5. s1.empty
print(s1.empty)