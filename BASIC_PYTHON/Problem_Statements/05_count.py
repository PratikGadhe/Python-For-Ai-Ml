"""
5. Count Vowels and Consonants
Problem Statement:
Create a program to count the number of vowels and consonants in a given string.
Input:
 A string
Output:
 Number of vowels and consonants
Example:
Input: "hello world"
Output: Vowels = 3, Consonants = 7
Note: Ignore spaces and special characters
"""
user = input("Enter a string : ")
vowels = 0
consonant = 0
for i in user :
    if i in "aeiou":
        vowels += 1
    elif i not in "aeiou":
        consonant += 1
    elif i in " !@#$%^&*()":
        continue
print(f"Vowels : {vowels} and Consonant : {consonant}")