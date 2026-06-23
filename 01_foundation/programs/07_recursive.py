"""
10. Recursive Sum of List
Problem Statement:
Write a recursive function to calculate the sum of all elements in a list.
Input:
 List of numbers
Output:
 Sum of elements
Example:
Input: [1, 2, 3, 4]
Output: 10
"""
l1 = [1,2,3,4]
def sum(list):
    n = len(list)-1
    if(n<0):
        return 0
    else:
        return list[n] + sum(list[:n])
print("Sum : ",sum(l1))