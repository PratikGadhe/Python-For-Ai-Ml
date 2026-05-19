"""
44. Swap First and Last Element of List
Problem Statement:
Develop a program to swap the first and last elements of a list.
Input:
 List
Output:
 Updated list
Example:
Input: [1, 2, 3]
Output: [3, 2, 1]
"""
n=[1,2,3]
n[0],n[len(n)-1]= n[len(n)-1],n[0]
print(n)