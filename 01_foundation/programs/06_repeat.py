"""
8. Most Frequent Word
Problem Statement:
Write a program to identify the most frequently occurring word in a given string.
Input:
 A string
Output:
 Word with highest frequency
Example:
Input: "cat dog cat bird dog cat"
Output: cat
"""
user = "cat dog cat bird dog cat"
split = user.split()
list = []
final = []
for i in split:
    if(i not in list):
        list.append(i)
    else:
        final.append(i)
print(final)