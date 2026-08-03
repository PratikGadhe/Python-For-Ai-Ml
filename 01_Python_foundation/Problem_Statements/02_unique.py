"""
2. Difference Between Two Lists
Problem Statement:
Write a program to find elements that are present in the first list but not in the second list.
Input:
 Two lists of integers
Output:
 A list containing elements unique to the first list
Example:
Input: L1 = [1, 2, 3, 4], L2 = [3, 4, 5]
Output: [1, 2]
"""
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5]
final = []
for i in l1:
    if i not in l2:
        final.append(i)
print(final)