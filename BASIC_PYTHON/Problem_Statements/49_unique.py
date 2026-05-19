"""
49. Count Unique Elements in List
Problem Statement:
Write a program to count unique elements in a list.
Input:
 List
Output:
 Count of unique elements
Example:
Input: [1,1,2,3]
Output: 3
"""
n = [1,1,2,3]
s = list(set(n))
print(len(s))