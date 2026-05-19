"""
59. Find Sum of Digits
Problem Statement:
Write a program to calculate sum of digits.
Input:
 Integer
Output:
 Sum
Example:
Input: 123
Output: 6
"""
n =(input("Enter a number : "))
sum = 0
for i in n:
    sum += int(i)
print(sum)