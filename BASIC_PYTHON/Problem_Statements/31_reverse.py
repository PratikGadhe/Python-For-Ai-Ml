"""
31. Reverse a List Without Using Built-in Functions
Problem Statement:
Write a program to reverse a list without using any built-in reverse functions.
Input:
 A list of elements
Output:
 Reversed list
Example:
Input: [1, 2, 3]
Output: [3, 2, 1]
"""

l1 = [1, 2, 3]
print(l1[::-1])

l1 = [1, 2, 3]

start = 0
end = len(l1) - 1

while start < end:
    l1[start], l1[end] = l1[end], l1[start]
    start += 1
    end -= 1

print(l1)