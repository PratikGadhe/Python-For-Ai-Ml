# some special methods 
import pandas as pd
import numpy as np

df = pd.DataFrame({'name':['pratik','sanket','vilas','archana'],
                   'marks':[90,80,np.nan,100],
                   'age':[21,24,50,47]},index=['A','A+','B','AB'])
print(df)
# 1. setting column name as index 
print(df.set_index('marks'))

# # 2. resetting index as column
print(df.reset_index())

# 3. renaming the columns name 
print(df.rename(columns={'name':'NAME','marks':'MARKS'}))

# 4. sorting the values by columns
print(df.sort_values(by=['name']))
print(df.sort_index())

# 5. to find whether there is NaN exist
print(df.isna())

# 6. to fill the NaN values 
print(df.fillna(99))

# 7. to find if all columns has non zero values or not 
print(df.all())

# 8.to find whether all columns has non zero 
print(df.any())

# 9.top 5 elements 
print(df.head(2))

# 10. bottom 5 elements
print(df.tail(2))

# 11. concatenation
df1 = pd.DataFrame({'name':['pratik','sanket','vilas','archana'],
                   'marks':[90,80,np.nan,100],
                   'age':[21,24,50,47]},index=['A','A+','B','AB'])
print(pd.concat([df,df1],ignore_index = True))  #vertically concatenation

print(pd.concat([df,df1],axis=1)) # horizontally