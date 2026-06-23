"""
17. Count Digits, Letters, and Special Characters
Problem Statement:
Develop a program to count the number of digits, alphabets, and special characters in a given
string.
Input:
 A string
Output:
 Count of digits, letters, and special characters
Example:
Input: "Hello123!"
Output: Letters = 5, Digits = 3, Special Characters = 1
"""
# 1. approach
string = "hello123!"
letter = 0
digit = 0
char = 0
for i in string:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        letter += 1
    elif 48 <= ord(i) <= 57:
        digit += 1
    else:
        char+=1
print(letter,digit,char)

# 2. approach
string = "hello123!"

letter = 0
digit = 0
char = 0

for i in string:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    else:
        char += 1

print("Letters =", letter)
print("Digits =", digit)
print("Special Characters =", char)