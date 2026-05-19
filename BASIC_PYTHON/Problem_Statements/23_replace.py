"""
23. Replace Elements in a List
Problem Statement:
Create a program to replace all occurrences of a specific element in a list with another
element.
Input:
 List
 Element to replace
 New element
Output:
 Updated list
Example:
Input: [1, 2, 3, 2], replace 2 with 9
Output: [1, 9, 3, 9]
"""
l1 = [1,2,3,2]
r = 2
k = 9
for i in range(len(l1)):
    if(l1[i] == r):
        l1[i]=k
print(l1)