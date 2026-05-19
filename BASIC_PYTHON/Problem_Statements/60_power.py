"""
60. Recursive Power Function
Problem Statement:
Develop a recursive function to compute power (xⁿ).
Input:
 Base x, exponent n
Output:
 Result
Example:
Input: x = 2, n = 3
Output: 8
"""
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 3))