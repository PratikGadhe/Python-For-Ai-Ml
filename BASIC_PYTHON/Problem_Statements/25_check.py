"""
25. Check if List is Sorted
Problem Statement:
Develop a program to check whether a list is sorted in ascending order.
Input:
 A list of numbers
Output:
 True / False
Example:
Input: [1, 2, 3, 4]
Output: True
"""
n = [1, 2, 3, 4]

for i in range(0,len(n)-1):
    if(n[i]<n[i+1]):
        condition = True
    else:
        condition = False
        break
print(condition)


# 2nd method
n = [1, 2, 3,0]

condition = True

for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
        condition = False
        break

print(condition)