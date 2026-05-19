"""
56. Find LCM of Two Numbers
Problem Statement:
Develop a program to find LCM of two numbers.
Input:
 Two integers
Output:
 LCM
Example:
Input: 4, 6
Output: 12
"""
n1 = 4
n2 = 6
def lcm(n1,n2):
    if(n1 > n2):
        highest = n1
    else :
        highest = n2
    while(True):
        if(highest%n1 == 0 and highest%n2 == 0):
            lcm = highest
            break
        highest += 1
    return lcm
print(lcm(n1,n2))
