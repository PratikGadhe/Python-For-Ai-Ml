"""
32. Find Minimum and Maximum in a List
Problem Statement:
Develop a program to find the minimum and maximum elements in a list.
Input:
 A list of numbers
Output:
 Minimum and maximum values
Example:
Input: [4, 1, 9, 2]
Output: Min = 1, Max = 9
"""
list1 = [4, 1, 9, 2]
list1.sort()
print("min : ",list1[0],", max",list1[len(list1)-1])

n = [4, 1, 9, 2]
max1 = n[0]
min1 = n[0]
for i in range(1,len(n)):
    if(max1 < n[i]):
        max1 = n[i]
    if(min1 > n[i]):
        min1 = n[i]

print(min1 , max1)