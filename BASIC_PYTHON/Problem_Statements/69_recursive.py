"""
69. Recursive Sum of Natural Numbers
Problem Statement:
Write a recursive function to calculate the sum of first n natural numbers.
Input:
 Integer n
Output:
 Sum
Example:
Input: n = 5
Output: 15
"""
n = int(input("Enter a number : "))
def natural(n):
    if(n<=0):
        return 0
    else:
        return n + natural(n-1)
result = natural(n)
print(result)