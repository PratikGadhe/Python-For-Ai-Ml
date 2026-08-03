"""
39. Generate Multiplication Table
Problem Statement:
Write a program to generate the multiplication table of a given number.
Input:
 Integer
Output:
 Multiplication table
Example:
Input: 2
Output: 2, 4, 6, 8, 10...
"""
n = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
