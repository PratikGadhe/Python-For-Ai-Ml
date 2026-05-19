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
str = input("Enter String : ")
if str == str[::-1]:
    print(True)
else:
    print(False)

# 2nd method 
string = "madam"
start = 0
end = len(string)-1
is_pallendrome = True
while(start < end):
    if(string[start] != string[end]):
        is_pallendrome = False
        break
    start += 1
    end -= 1
print(is_pallendrome)