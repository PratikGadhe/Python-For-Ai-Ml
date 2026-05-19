"""
7. Merge Lists into Dictionary
Problem Statement:
Develop a program to create a dictionary by combining two lists: one containing keys and the
other containing corresponding values.
Input:
 List of keys
 List of values
Output:
 Dictionary mapping keys to values
Example:
Input: Keys = ["a", "b"], Values = [1, 2]
Output: {"a":1, "b":2}
Constraint:
 Both lists must be of equal length
"""

keys = ["a", "b"]
values = [1, 2]
dict = {}
for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)
