"""
36. Find Index of Element in List
Problem Statement:
Develop a program to find the index of a given element in a list.
Input:
 List
 Element to search
Output:
 Index of element or "Not Found"
Example:
Input: [10, 20, 30], element = 20
Output: 1
"""

n = [10, 20, 30]
key = 20
index = 0
for i in range(len(n)):
    if n[i] == key:
        index = i
if key not in n:
    print("key not found !")
else:
    print(index)
