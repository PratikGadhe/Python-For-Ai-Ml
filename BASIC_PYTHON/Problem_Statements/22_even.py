"""
22. Find All Even Numbers in a List
Problem Statement:
Write a program to extract all even numbers from a given list.
Input:
 A list of integers
Output:
 List of even numbers
Example:
Input: [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]
"""
l1 = [1,2,3,4,5,6]
even = []
for i in l1:
    if(i%2 == 0):
        even.append(i)
print(even)