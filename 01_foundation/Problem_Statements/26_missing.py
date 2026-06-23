"""
26. Find Missing Number in a Sequence
Problem Statement:
Write a program to find the missing number in a given sequence of consecutive integers.
Input:
 List of integers with one missing number
Output:
 Missing number
Example:
Input: [1, 2, 4, 5]
Output: 3
"""

# n = [1, 2, 4, 5]
# for i in range(len(n)):
#     if n[i] == i + 1:
#         pass
#     else:
#         print(i + 1)
#         break
n = [4, 1, 2, 5]
n.sort()
for i in range(len(n)-1):
    if n[i+1] - n[i] != 1:
        print(n[i] + 1)
        break