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
lst = [1, 2, 2, 3, 4, 3]
duplicate = list((set(lst)))
print(duplicate)

# another
lst1 = []
for i in lst:
    if(i not in lst1):
        lst1.append(i)
    else:
        continue
print(lst1)