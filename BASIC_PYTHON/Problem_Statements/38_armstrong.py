"""
38. Check Armstrong Number
Problem Statement:
Create a program to check whether a number is an Armstrong number.
Input:
 Integer
Output:
 True / False
Example:
Input: 153
Output: True
"""
n = input("Enter a number : ")
power = len(n)
result = 0
for i in n:
    result += int(i)**power
if(result == int(n)):
    print(True)
else:
    print(False)