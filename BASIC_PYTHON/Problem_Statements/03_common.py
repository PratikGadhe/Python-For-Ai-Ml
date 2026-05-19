"""
3. Common Elements in Three Lists
Problem Statement:
Develop a program to identify elements that are common across three given lists.
Input:
 Three lists
Output:
 List of common elements
Example:
Input: [1,2,3], [2,3,4], [2,5,3]
Output: [2, 3]
"""
l1 = [1,2,3]
l2 = [2,3,4]
l3 = [2,5,3]
common = []
for i in l1 :
    if i in l2 and l3:
        common.append(i)
print(common)