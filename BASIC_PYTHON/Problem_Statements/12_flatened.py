"""
12. Flatten Nested List
Problem Statement:
Write a program to convert a nested list into a single flattened list.
Input:
 Nested list
Output:
 Flattened list
Example:
Input: [1, [2, [3, 4]], 5]
Output: [1, 2, 3, 4, 5]
"""
# string=input("string:")
# s=string.split()
# d={}
# for word in s:
#     key=word[0]
#     if key in d:
#         d[key].append(word)
#     else:
#         d[key]=[word]
# print(d)
# input 
lst = "I am Pratik"
dict1= {}
string = ""
count = 0
for i in lst:
    if( i != " "):
        string += i
    else:
        if(string in dict1):
            dict1[string]+=1
        else:
            dict1[string]=1
        string = ""
print(dict1)