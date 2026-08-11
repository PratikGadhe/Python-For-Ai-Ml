# write operation
import pandas as pd
import numpy as np
# creating dataframe and saving it into csv file
df = pd.DataFrame({'roll':[1,2,3,4],
                   'name':['pratik','sanket','archana','vilas'],
                   'age':[21,24,47,50]})
print(df)
# saving it into csv file
df.to_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_pandas/03_csv/student.csv")

# copying the one csv file data to another
df1 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/employee.csv")
print(df1)
df1.to_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/new_employee.csv")

# modifying the existing data of csv file

df3 = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/new_employee.csv")
print(df3)
df3.loc[2,'empid']= 111.0
print(df3)
df3.to_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/03_Pandas/03_csv/new_employee.csv")