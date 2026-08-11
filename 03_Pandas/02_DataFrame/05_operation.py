import pandas as pd
import numpy as np
df1 = pd.DataFrame({'test 1':[5,6,8,3,10],
                   'test 2':[7,8,9,6,15]})
df2 = pd.DataFrame({'test 1':[3,3,6,6,8],
                   'test 2':[5,9,8,10,5]})
# operations in dataframe
# 1. concatenation : pd.concat([])
print(pd.concat([df1,df2],ignore_index = True))

# 2. addition : df1.sum(df2)
print(df1.add(df2))

# 3. subtraction : df1.sub(df2)
print(df1.sub(df2))

# 4. reverse subtraction : df1.rsub(df2)
print(df1.rsub(df2))

# 5. multiplication : df1.mul(df2)
print(df1.mul(df2))

# 6. division : df1.div(df2)
print(df1.div(df2))

# 7. arithmetic operation without methods
print(df1+df2)
print(df1-df2)
print(df1*df2)
print(df1/df2)

# 8. dataframe with consant value
print(df1+10)
