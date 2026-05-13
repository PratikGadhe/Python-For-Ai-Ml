# creating empty data frame 
import pandas as pd
import numpy as np 
df = pd.DataFrame()
print(df)

y1 = {'q1':5000,'q2':8000,'q3':12000,'q4':18000} #series 1
y2 = {'a':13000,'b':14000,'c':12000} #series 2
total = {1:y1,2:y2} #final series
df = pd.DataFrame(total)
print(df)

# creating a dataframe using list 

l1 = [1,2,3,4,5]
col = ["pratik"]
index = ['a','b','c','d','e']
df = pd.DataFrame(l1 , index = index , columns = col)
print(df)

# creating dataframe using nested list 
l1 = [80,90,70]
l2 = [75,95,67]
l3 = [79,89,80]
student = [l1,l2,l3]
print(student)
df = pd.DataFrame(student,columns = ["s1",'s2','s3'],index=['phy','chem','math'])
print(df)

# creating a dataframe using single series
s1 = pd.Series([10,20,30,40,50])
df = pd.DataFrame(s1)
print(df)

# creating a dataframe usinng series and passing it in df as list
s2 = pd.Series([1,2,3,4,5])
df = pd.DataFrame([s1,s2])
print(df)

# creating dataframe using series and dictionary 
s1 = pd.Series([10,20,30,40,50])
s2 = pd.Series([1,2,3,4,5])
df = pd.DataFrame({'ST1':s1,'ST2':s2},index = [0,1,2,3,4])
print(df)

# creating dataframe usinf dictionary of list

dict_of_list = {"Name" : ["Pratik",'Vilas','Sanket','Archana'],"Salary" :[6000,15000,11000,75000],"age":[20,48,23,43]}
df = pd.DataFrame(dict_of_list,index=[1,2,3,4])
print(df)

# creating dataframe using dictionary of series 
name = pd.Series(["Pratik","Sanket",'Vilas','Archana'])
salary = pd.Series([6000,75000,15000,11000])
age = pd.Series([20,23,48,43])
df = pd.DataFrame({"Name" : name ,"Salary" : salary ,"age":age})
print(df)

# creating dataframe using list of dictionary

new = [{'Name':"Pratik",'Salary':6000,'Age':20},
       {'Name':"Sanket",'Salary':75000,'Age':23}]
df = pd.DataFrame(new)
print(df)

# creating Dataframe using numpy ndarray
array = np.array([["Pratik",6000,20],["Sanket",75000,23]])
cols = ["Name",'Salary','Age']
index = [1,2]
df = pd.DataFrame(data =array , columns = cols , index = index)
print(df)

df = pd.DataFrame({"name":["Pratik","Sanket",],"age":[20,np.nan]},index=['a','b'])
print(df)

# Attributes in dataframe 1. index
print(df.index)
# 2. columns
print(df.columns)
# 3.axes
print(df.axes)
# 4.dtypes
print(df.dtypes)
# 5.size (rows * columns)
print(df.size)
# 6.shape
print(df.shape)
# 7.ndim
print(df.ndim)
# 8.empty
print(df.empty)
# 9.T (transpose)
print(df.T)


# method in dataframe : df.isna()
print(df.isna())

# setting column as index 
df.set_index("name",inplace = True)
print(df)

# resetting  index as column
df.reset_index(inplace = True)
print(df)


s1 = pd.Series(["Rinku",'ritu','ajay','pankaj','aaditya'])
s2 = pd.Series([67,78,75,88,92])
s3 = pd.Series([78,67,89,90,56])
s4 = pd.Series([78,88,98,90,87])
s5 = pd.Series([77,70,80,67,86])
df = pd.DataFrame({"name":s1,"eng":s2,"eco":s3,'ip':s4,'acct':s5})
print(df)
# acessing single element using index position (.iat[])
print(df.iat[1,3])

# acessing single element using index label (.at[])
print(df.at[3,"name"])

# adding new row using .loc[index label]
df.loc[5]=["pratik",90,80,95,78]
print(df)

# modifying the row usinf .loc
df.loc[5]=["Sanket",90,80,95,91]
print(df)

df.rename(columns = {"name":"NAME"},inplace=True)
print(df)

df['total']=df['eng']+df['eco']+df['ip']+df['acct']
print(df)
df['surname']=['sharma','giramkar','atul','tripathi','aadhave','gadhe','gadhe']
print(df)

df.insert(7,'age',[43,20,57,58,21,20,23])
print(df)

print(df["NAME"])
print(df.surname)


df.rename(columns = {"surname":"SURNAME"},inplace = True)
print(df.iloc[0:6,0:6])

del df["acct"]
print(df)
print(df.pop("total"))
print(df)

df = pd.DataFrame()
df['name']=['shruti','gunjan','tanya']
df['phy']=[90,80,88]
df['chem']=[90,80,88]
df['total']=df['phy']+df['chem']
print(df)

# head function in dataframe
s1 = pd.Series(["Rinku",'ritu','ajay','pankaj','aaditya'])
s2 = pd.Series([67,78,75,88,92])
s3 = pd.Series([78,67,89,90,56])
s4 = pd.Series([78,88,98,90,87])
s5 = pd.Series([77,70,80,67,86])
df = pd.DataFrame({"name":s1,"eng":s2,"eco":s3,'ip':s4,'acct':s5})
print(df)

print(df.head(2))
print(df.tail(-3))
print(df[2:4])

# concatenation in dataframe
d1 = {"roll_no":[10,11,12,13,14,15],"name":["ankit","pihu","rinku","yash","vijay","khushi"]}
d2 = {"roll_no":[20,21,22,23,24,25],"name":["shaurya","pinky","anubhav","khushi","vinay","neetu"]}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
# df3 = df1 + df2
df3 = pd.concat([df1,df2],ignore_index = True,axis = 1)
print(df3)

# end of pandas dataframe