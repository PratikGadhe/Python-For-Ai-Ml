"""
66. Find Common Keys in Two Dictionaries
Problem Statement:
Develop a program to find common keys present in two dictionaries.
Input:
 Two dictionaries
Output:
 List of common keys
Example:
Input: {'a':1, 'b':2}, {'b':3, 'c':4}
Output: ['b']
"""
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

common = []

for key in d1:
    if key in d2:
        common.append(key)

print(common)