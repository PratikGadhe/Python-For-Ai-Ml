"""
28. Merge Two Dictionaries
Problem Statement:
Write a program to merge two dictionaries into one.
Input:
 Two dictionaries
Output:
 Combined dictionary
Example:
Input: {'a':1}, {'b':2}
Output: {'a':1, 'b':2}
"""
# Input dictionaries
dict1 = {'a': 1}
dict2 = {'b': 2}

# Method 1: Using update()
merged_dict = dict1.copy()   # copy to avoid changing original
merged_dict.update(dict2)

# Output
print(merged_dict)