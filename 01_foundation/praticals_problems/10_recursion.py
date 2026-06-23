"""
wap to find the length of list using recursion
"""

# 1. list slicing
n = [1,2,3,4,5]
def length(n):
    if n == []:
        return 0
    return 1 + length(n[1:])
result = length(n)
print(result)

# 2. index method 
n = [1,2,3,4,5]
def length(n,index = 0):
    if(index == len(n)):
        return 0
    return 1 + length(n , index + 1)
result = length(n)
print(result)

# 3. count method 
n = [1,2,3,4,5]
def length(n,count = 0):
    if n == []:
        return count
    return length(n[1:] , count + 1)
result = length(n)
print(result)