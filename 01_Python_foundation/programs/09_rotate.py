"""
13. Rotate List
Problem Statement:
Create a program to rotate a list by k positions to the right.
Input:
 List
 Integer k
Output:
 Rotated list
Example:
Input: [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""
list = [1,2,3,4,5]
k = 2
def rotate(list,k):
    l1 = list[:k+1]
    l2 = list[k+1:]
    return l2+l1
print(rotate(list,k))