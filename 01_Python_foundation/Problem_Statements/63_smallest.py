"""
63. Find Smallest Element in a List Using Recursion
Problem Statement:
Write a recursive function to find the smallest element in a list.
Input:
 A list of numbers
Output:
 Smallest element
Example:
Input: [5, 2, 9, 1]
Output: 1
"""
def find_min(lst):
    # Base case
    if len(lst) == 1:
        return lst[0]
    
    # Recursive call
    smallest = find_min(lst[1:])
    
    # Compare
    if lst[0] < smallest:
        return lst[0]
    else:
        return smallest


# Example
print(find_min([5, 2, 9, 1]))