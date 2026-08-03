"""
54. Convert Decimal to Binary
Problem Statement:
Create a program to convert a decimal number to binary.
Input:
 Integer
Output:
 Binary representation
Example:
Input: 5
Output: 101
"""
n = 25
print(bin(n)[2:])
binary = ""
while(n>0):
    rem = n%2
    binary = str(rem) + binary
    n = n//2
print(binary)