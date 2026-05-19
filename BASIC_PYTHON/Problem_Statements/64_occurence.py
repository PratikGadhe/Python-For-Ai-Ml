"""
64. Count Occurrence of a Character in String
Problem Statement:
Create a program to count how many times a specific character appears in a string.
Input:
 A string
 A character
Output:
 Count of occurrences
Example:
Input: "banana", character = 'a'
Output: 3
"""
string = "banana"
ch = 'a'

count = string.count(ch)

print(count)