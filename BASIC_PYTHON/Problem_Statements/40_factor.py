"""
40. Find All Factors of a Number
Problem Statement:
Develop a program to find all factors of a given number.
Input:
 Integer
Output:
 List of factors
Example:
Input: 6
Output: [1, 2, 3, 6]
"""
n = int(input("Enter a number : "))
result = []
for i in range(1,n+1):
    if(n%i == 0):
        result.append(i)
print(result)