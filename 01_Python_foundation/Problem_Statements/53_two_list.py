"""
53. Check if Two Lists are Equal
Problem Statement:
Write a program to check if two lists are equal.
Input:
 Two lists
Output:
 True / False
Example:
Input: [1,2], [1,2]
Output: True
"""
n1 = [1,2]
n2 = [1,2]
for i in range(len(n1)):
    if(n1[i] == n2[i]):
        result = True
    else :
        result = False
        break
print(result)