"""
51. Replace Spaces with Hyphens
Problem Statement:
Write a program to replace spaces in a string with hyphens.
Input:
 String
Output:
 Modified string
Example:
Input: "hello world"
Output: "hello-world"
"""
string = "hello word"
for i in string:
    if (i == " "):
        print(string.replace(" ",'-'))
