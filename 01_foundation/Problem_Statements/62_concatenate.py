"""
62. Concatenate Two Strings Without Using ‘+’ Operator
Problem Statement:
Develop a program to concatenate two strings without using the ‘+’ operator.
Input:
 Two strings
Output:
 Concatenated string
Example:
Input: "Hello", "World"
Output: "HelloWorld"
"""
s1 = "Hello"
s2 = "World"

result = ""

for ch in s1:
    result += ch

for ch in s2:
    result += ch

print(result)