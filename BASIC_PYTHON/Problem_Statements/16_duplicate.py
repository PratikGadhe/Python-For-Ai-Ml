"""
16. Remove Duplicate Elements from a List
Problem Statement:
Write a program to remove duplicate elements from a list while maintaining the original
order.
Input:
 A list of elements
Output:
 List with duplicates removed
Example:
Input: [1, 2, 2, 3, 4, 3]
Output: [1, 2, 3, 4]
"""
list1 = [1,2,2,3,4,3]
result = []
for i in list1:
    if i not in result:
        result.append(i)
print(result)