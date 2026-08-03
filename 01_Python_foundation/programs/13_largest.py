"""
18. Find Second Largest Element in a List
Problem Statement:
Write a program to find the second largest element in a list without sorting the list.
Input:
 A list of integers
Output:
 Second largest number
Example:
Input: [10, 20, 4, 45, 99]
Output: 45
Constraint:
 List must contain at least two unique elements
"""
lst = [10,20,100,45,99]
lst1 = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[j]>lst[i]):
            lst[i],lst[j]=lst[j],lst[i]
print(lst[1])
