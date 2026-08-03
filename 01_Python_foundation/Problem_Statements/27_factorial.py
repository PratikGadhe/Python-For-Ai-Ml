"""
27. Recursive Factorial Program
Problem Statement:
Develop a recursive function to calculate the factorial of a number.
Input:
 Integer n
Output:
 Factorial of n
Example:
Input: 5
Output: 120
"""
n = int(input("Enter a number : "))
def factorial(n):
    if(n<=0):
        return 1
    else:
        return n * factorial(n-1)
result = factorial(n)
print(result)