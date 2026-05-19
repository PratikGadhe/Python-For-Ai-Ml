"""
wap to create a dictionary with key as first character and value as word
"""
# 1. manual method
n = input("Enter a string : ").split()
print(type(n))
dict1 = {}
for i in n:
    key = i[0]
    if(key in dict1):
        dict1[key].append(i)
    else:
        dict1[key] = [i]
print(dict1)

# 2. set default() method
n = "apple banana cherry blueberry"
lst = n.split()
dict1 = {}
for i in lst:
    key = i[0]
    dict1.setdefault(key,[]).append(i)
print(dict1)

# 3. comprehension method
n = "apple banana blueberry cherry"
lst = n.split()
dict1 = {}
result = [dict1.setdefault(i[0],[]).append(i) for i in lst]
print(dict1)