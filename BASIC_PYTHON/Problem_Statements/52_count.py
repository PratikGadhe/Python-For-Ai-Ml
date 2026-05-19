"""
52. Count Frequency of Elements in List
Problem Statement:
Develop a program to count frequency of elements in a list.
Input:
 List
Output:
 Dictionary of frequencies
Example:
Input: [1,1,2]
Output: {1:2, 2:1}
"""

n = [1, 1, 2]
dict = {}
for i in n:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
