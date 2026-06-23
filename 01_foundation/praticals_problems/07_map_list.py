"""
wap to map two list into dictionary
"""
# 1. manual method
key = ['A','B','C']
values = ["Apple","Banana","Cherry"]
dict1 = {}
for i in range(len(key)):
    dict1[key[i]]= values[i]
print(dict1)

# 2. zip() method
key = ['A','B','C']
values = ["Apple","Banana","Cherry"]
dict1 = dict(zip(key,values))
print(dict1)

# 3. comprehension method
key = ['A','B','C']
values = ["Apple","Banana","Cherry"]
dict1 = {key[i] : values[i] for i in range(len(key))}
print(dict1)

# 4. enumerate method
key = ['A','B','C']
values = ["Apple","Banana","Cherry"]
dict1 = { key : values[i] for i,key in enumerate(key)}
print(dict1)