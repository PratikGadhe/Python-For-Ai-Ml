import numpy as np
# FILTERING THE ARRAY
number = np.array([1,2,3,4,5,6,7,8,9,10])
even = number[1::2] #slicing method
print("By Slicing : ",even)
# numpy allows the expression to be written in []
even_f = number[number%2 == 0]
print("By Filtering : ",even_f)
# filtering by mask 
mask = (number%2 == 0)
e1 = number[mask]
print("filtering by mask : ",e1)

# FANCING INDEXING VS WHERE CLAUSE 
index = [2,4,6]
print("index : ",number[index]) 

where_clause = np.where(number>3)
print("values greater than 3: ",number[where_clause])


# CONDITION ARRAY USING WHERE METHOD 
# syntax : np.where(<condition> , <if true > , <else false> )
condition_array = np.where(number > 3 , "true" , "false")
print(condition_array)