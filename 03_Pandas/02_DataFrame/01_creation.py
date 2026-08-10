import pandas as pd
import numpy as np

# 1. dataframe using nested list (list of list)
d1 = pd.DataFrame([['shreya',20],['rakshit',22],['srijan',18]])
print(d1) 
# no. of list == row and no. of elements in single list == columns

# 2. dataframe using series 
# a. no. of series == no. of rows in dataframe
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([10,20,30,40])
d2 = pd.DataFrame([s1,s2]) #list of series = row/horizontally
print(d2)
# b. if want to show in vertically than use dict of series
d3 = pd.DataFrame({'s1':s1,'s2':s2}) #dict of series = vertically/column
print(d3)

# 3. dataframe using dictionary
# a. dictionary of list method :
list1 = [37,41,50,62]
list2 = ['aaditya','tushar','shubham','pratik']
d4 = pd.DataFrame({'Roll_no':list1,'Name':list2},index = [1,2,3,4])
print(d4)

# b. dictionary of series 
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([10,20,30,40])
d5 = pd.DataFrame({'s1':s1,'s2':s2})
print(d5)

# c. list of dictionry 
dict1 = {'roll no': 1 , 'name': 'Pratik'}
dict2 = {'roll no' : 2 , 'name':'sanket'}
d6 = pd.DataFrame([dict1,dict2],index=[1,2])
print(d6)

# 4. datafame using numpy array
array = np.array([[1,2,3],
                  [3,4,5],
                  [6,7,8]])
d7 = pd.DataFrame(array)
print(d7)