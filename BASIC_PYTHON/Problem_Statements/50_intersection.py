"""
50. Find Intersection Without Built-in Functions
Problem Statement:
Create a program to find intersection of two lists without using built-in functions.
Input:
 Two lists
Output:
 Intersection list
Example:
Input: [1,2,3], [2,3,4]
Output: [2,3]
"""
n1 = [1,2,3]
n2 = [2,3,4]
arr = []
for i in range(len(n1)):
    for j in range(len(n1)):
        if(n1[i] == n2[j]):
            arr.append(n1[i])
print(arr)


# 2nd method
n1 = [1,2,3]
n2 = [2,3,4]
arr = []

for i in n1:
    if i in n2:
        arr.append(i)
print(arr)

intersect  = [x for x in n1 if x in n2]
print(intersect)