"""
48. Check Subset of List
Problem Statement:
Develop a program to check whether one list is a subset of another.
Input:
 Two lists
Output:
 True / False
Example:
Input: [1,2], [1,2,3]
Output: True
"""
n = [1,2,3]
a = [1,2]
for i in a :
    if(i in n):
        condition = True
    else:
        condition = False
print(condition)