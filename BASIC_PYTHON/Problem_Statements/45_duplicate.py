"""
45. Find Duplicate Elements in List
Problem Statement:
Write a program to identify duplicate elements in a list.
Input:
 List
Output:
 List of duplicate elements
Example:
Input: [1, 2, 2, 3]
Output: [2]
"""
n = [1, 2, 2, 3]

seen = []
duplicates = []

for i in range(len(n)):
    if n[i] in seen and n[i] not in duplicates:
        duplicates.append(n[i])
    else:
        seen.append(n[i])

print(duplicates)