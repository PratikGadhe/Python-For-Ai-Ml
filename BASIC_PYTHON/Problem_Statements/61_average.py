"""
61. Find Average of Elements in a List
Problem Statement:
Write a program to calculate the average of all elements in a list.
Input:
 A list of numbers
Output:
 Average value
Example:
Input: [2, 4, 6, 8]
Output: 5.0
"""
n = [2,4,6,8]
sum = 0
for i in n:
    sum += i
print(sum/(len(n)))