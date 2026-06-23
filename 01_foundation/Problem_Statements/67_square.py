"""
67. Create List of Squares
Problem Statement:
Write a program to create a list containing squares of numbers from 1 to n.
Input:
 Integer n
Output:
 List of squares
Example:
Input: n = 4
Output: [1, 4, 9, 16]
"""
n = int(input("Enter a number : "))
arr = []
for i in range(1,n+1):
    arr.append(i**2)
print(arr)