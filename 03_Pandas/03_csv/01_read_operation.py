# read operations
import pandas as pd
import numpy as np
# 1.reading csv file into pandas
df = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv")
print(df)

# 2. use specific columns
df1 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv",usecols = ['empid','name'])
print(df1)

# 3. select specific rows
df2 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv",nrows = 4)
print(df2)

# 4. without header
df3 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv",header = None)
print(df3)

# 5. without index
df4 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv",index_col = 0)
print(df4)

# 6. giving new columns name to csv data
df5 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv",skiprows = 1 , names = ['EMPID','NAME','AGE','CITY','SALARY'])
print(df5)