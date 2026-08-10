import pandas as pd
import numpy as np
name = ['rinku','ritu','ajay','pankaj','aditya']
marks = [67,78,75,88,90]
df = pd.DataFrame({'name':name,'marks':marks})
print(df)
# 1.retrieving / accessing rows 
print(df[2:])
print(df[:])
print(df[::-1])
print(df[1:4])

# 2.accessing single values from dataframe
# df.iat[<row>,<column>]
print(df.iat[2,1])
# df.at[<row_index>,<column_index]
print(df.at[2,'marks'])

# 3. adding/modifying row in a dataframe 
#  df.loc[<row label>]=[values]
df.loc['5']=['sachin',69]
df.loc['6']=['shubham',90]
df.loc['7']=['pratik',95]
print(df)

# 4. adding columns into dataframe
# syntax = df['name']=['values']
df['cgpa']=[7,8,9,10,8,6,7,5,9]
print(df)

df['total']=df['marks']+df['cgpa']
print(df)

# insert method
df.insert(4,'gender',['f','f','m','m','m','m','m','m','m'])
print(df)

# selecting the columns
# using .iloc[] and .loc[]
print(df.iloc[:,1:4])
print(df.iloc[0:4,[1,4]])

# loc[<columns index number> : <column index number>]
print(df.loc[1:3])