"""
42. Check Prime Number
Problem Statement:
Create a program to check whether a number is prime.
Input:
 Integer
Output:
 True / False
Example:
Input: 7
Output: True
"""
n = int(input("Enter a number : "))
for i in range(2,n):
    if(n%i != 0):
        prime = True
    else:
        prime = False
        break
print(prime)