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
list1 = [1,2,3,4,5]
k = int(input("Enter value of k to rotate a list : "))
# start = list1[k+1:]
# end = list1[:k+1]
# final = start + end
# print(final)
def rotate(list,k):
    start = list[k+1:]
    end = list[:k+1]
    return start + end
result = rotate(list1,k)
print("After rotate : ",result)