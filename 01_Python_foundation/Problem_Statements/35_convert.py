"""
35. Convert List to String
Problem Statement:
Write a program to convert a list of characters into a single string.
Input:
 List of characters
Output:
 Combined string
Example:
Input: ['P','y','t','h','o','n']
Output: "Python"
"""
n = ['P','y','t','h','o','n']
str = ""
for i in n:
    str += i
print(str)