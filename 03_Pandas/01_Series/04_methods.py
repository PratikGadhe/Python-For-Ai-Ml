# methods used in series
import pandas as pd
import numpy as np
s1 = pd.Series([10,20,30,40,50,np.nan],index = ['p','r','a','t','i','k'])
# 1. series.head() : shows the top elements
print(s1.head()) #top 5 elements
print(s1.head(3)) # top 3 elements
print(s1.head(-2)) # cannot consider last 2 elements

# 2. series.tail() : shows the bottom elements
print(s1.tail()) #bottom 5 elements
print(s1.tail(3)) #bottom 3 elements
print(s1.tail(-2)) #cannot consider first 2 elements

# 3. series.count() : count the non-nan value 
print(s1.count())   #5:non nan value
print(s1.size)      #6: with nan value