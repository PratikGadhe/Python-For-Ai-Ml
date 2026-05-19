"""
55. Find GCD of Two Numbers
Problem Statement:
Write a program to find GCD of two numbers.
Input:
 Two integers
Output:
 GCD
Example:
Input: 8, 12
Output: 4
"""
a = 8
b = 12

while b != 0:
    a, b = b, a % b
print(a)