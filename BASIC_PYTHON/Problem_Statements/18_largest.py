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
# with sorting method 
list1 = [10, 20, 4, 45, 99]
max = []
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[j] > list1[i]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1[1])

# without sorting method
list1 = [10, 20, 4, 45, 99]
largest = float('-inf')
second = float('-inf')

for num in list1:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest:", second)