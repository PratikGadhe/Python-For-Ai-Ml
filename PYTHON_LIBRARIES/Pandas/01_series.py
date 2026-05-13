import pandas as pd
import numpy as np
# creating an empty series
# s1 = pd.Series()
# print(s1)

#creating series using list 
# s1 = pd.Series([1,2,3,4,5],['a','b','c','d','e'])
# print(s1)

# creating using two list
months=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
no_days=[31,28,31,30,31,30,31,30,30,31,30,31]

# s1 = pd.Series(no_days,index=months)
# print(s1)

s1=pd.Series(range(10))
print(s1)

s2=pd.Series(range(1,15,3),index = [x for x in 'abcde'])
print(s2) 


s3 = pd.Series([1,2,3,0.5])
print(s3)
s3.index =['a','b','c','d']
print(s3)

# creating series using scalar and constant value
s4 = pd.Series(63,index=[1,23,91,11])
print(s4)
s5=pd.Series(63,index = range(1,15,3))
print(s5)

# creating series using string as data
s6 = pd.Series("welcome to pandas",index=["Pratik","Sanket","Gadhe"])
print(s6) 

# creating a series using dictionary
s6 = pd.Series({'P':"Pratik",'V':"Vilas",'G':"Gadhe"})
print(s6)

d1 = {'P':"Pratik",'V':"Vilas",'G':"Gadhe"}
s1=pd.Series(d1)
print(s1)


d2 = {'A':['p','v','g'],'B':{'p':'pratik'}}
s1 = pd.Series(d2)
print(s1)

s1 = np.arange(10,15)
s_obj = pd.Series(index = s1*4 , data = s1)
print(s_obj)

s2 = pd.Series([1,0.5,np.nan,0])
print(s2)

s1=pd.Series(data = [x for x in range(2,21,2)] , index = [x for x in range(0,10)])
print(s1)

array = np.array([1,2,3,4,5])
s1 = pd.Series(array)
print(s1)

s1 = pd.Series({'a':1,'b':2,'c':3})
s1.index.name = "ABCD"
s1.name = "123"
print(s1)

s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[:3])
print(s[:-3])
print(s[-3:])
print(s[:])
print(s[::-2])
print(s[0::2])

# iloc
print(s.iloc[-3:12])

# loc
print(s.loc['a':'o'])

# series attributes

s = pd.Series([1,2,3,np.nan,5,6],index=['p','r','a','t','i','k'])
print(s)
print(s.index)
print(s.values)
print(s.size)
print(s.hasnans)
print(s.empty)

# retrieving a series 1. head(n) 2.tail(n) 3.count()
s = pd.Series([1,2,3,np.nan,5,6],index=['p','r','a','t','i','k'])
print(s.head(2))
print(s.tail())
print(s.head(-2)) #prints all element except the last two elements
print(s.tail(-2))
print(s.count()) #count the number of non nan values 
print(s.size) #counts the length of series 

# mathematical expressions on series 
s = pd.Series([11,12,13,14],index=[2,1,3,4])
s1 = pd.Series([21,22,23,24],index=[2,1,3,4])
s3 = pd.Series([11,12,13,14],index=[101,102,103,104])
s4 = pd.Series([10,10,10,10],index=[10,102,103,4])
print(s1-s)
print(s+s3)
print(s3-s4)
print(s3*s)

# vector operations
print(s+2)
print(s*2)
print(s<15)
print(s**2)

print(s)
print(s[s<20])

print(s.drop(2,inplace=True))
print(s)
print(s.drop([1,4],inplace = True))
print(s)

s = pd.Series([1,2,3,np.nan,5,6,6],index=['p','r','a','t','i','k','a'])
print(s.dropna(inplace = True))
print(s)
print(s.drop_duplicates(inplace = True))
print(s)

# END OF SERIES IN PANDAS