"""
24. Count Uppercase and Lowercase Letters
Problem Statement:
Write a program to count the number of uppercase and lowercase letters in a string.
Input:
 A string
Output:
 Count of uppercase and lowercase letters
Example:
Input: "Hello World"
Output: Uppercase = 2, Lowercase = 8
"""
string = "Hello World"
upper = 0
lower = 0
for i in range(len(string)):
    if(65 <= ord(string[i]) <= 90):
        upper += 1
    elif(97<= ord(string[i])<=122):
        lower += 1
print("uppercae = ",upper,", ","lowercase = ",lower)
