"""
37. Sum of Even and Odd Numbers Separately
Problem Statement:
Write a program to calculate the sum of even and odd numbers separately.
Input:
 List of integers
Output:
 Sum of even numbers, sum of odd numbers
Example:
Input: [1, 2, 3, 4]
Output: Even = 6, Odd = 4
"""
n = [1,2,3,4]
even = []
odd = []
for i in n:
    if(i%2 == 0):
        even.append(i)
    else:
        odd.append(i)
print("even : ",sum(even)," , odd : ",sum(odd))