"""
30. Recursive Fibonacci Series
Problem Statement:
Write a recursive program to generate Fibonacci series up to n terms.
Input:
 Integer n
Output:
 Fibonacci sequence
Example:
Input: 5
Output: 0, 1, 1, 2, 3
"""
n = int(input("Enter a number : "))
n = int(input("Enter number of terms: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(n):
    print(fibonacci(i), end=" ")