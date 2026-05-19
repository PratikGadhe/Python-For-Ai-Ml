"""
41. Remove Empty Strings from List
Problem Statement:
Write a program to remove all empty strings from a list.
Input:
 List containing strings
Output:
 Updated list
Example:
Input: ["a", "", "b"]
Output: ["a", "b"]
"""
n = ["a", "", "b"]
a = []
for i in n:
    if(i != ""):
        a.append(i)
print(a)