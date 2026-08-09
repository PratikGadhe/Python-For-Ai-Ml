# operation can be performed in between series 
import pandas as pd
import numpy as np
s1 = pd.Series([10,20,30],index=['a',2,3])
s2 = pd.Series([20,30,40],index = [1,2,3])
s3 = pd.Series([30,40,50],index=[0,1,2])
# note : index should same otherwise nan pops up
# 1. arithmetic operation : (+ - * ÷)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s1+s2+s3)

# vector operation : 
print(s1+2)
print(s1 < 30)
print(s1[s1<30])