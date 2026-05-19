"""
57. Remove nth Element from List
Problem Statement:
Write a program to remove the nth element from a list.
Input:
 List
 Position n
Output:
 Updated list
Example:
Input: [1,2,3], n = 1
Output: [1,3]
"""
n = [1,2,3]
index = 1
n.pop(index)
print(n)