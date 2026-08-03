"""
11. Palindrome Check
Problem Statement:
Develop a program to check whether a given string is a palindrome.
Input:
 A string
Output:
 True / False
Example:
Input: "madam"
Output: True
"""
user = input("Enter a string : ")
# if(user == user[::-1]):
#     print("True")
# else:
#     print("False")

# 2nd method
pallendrome = True
start = 0
end = len(user)-1
while(start < end):
    if(user[start] != user[end]):
        pallendrome = False
        break
    start+=1
    end-=1
print(pallendrome)
