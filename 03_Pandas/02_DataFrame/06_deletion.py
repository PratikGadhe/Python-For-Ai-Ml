import pandas as pd
import numpy as np

df = pd.DataFrame({"roll no":[1,2,3,4,5],
                   "name":['shruti','gunjan','taniya','kirti','vineet'],
                   'phy':[80,90,70,88,95],
                   'chem':[56,86,66,77,98],
                   })
print(df)
# 1. del df[name]
del df['chem']
print(df)

print(df.pop('phy'))
print(df)

# drop method 
print(df.drop('roll no',axis = 1))