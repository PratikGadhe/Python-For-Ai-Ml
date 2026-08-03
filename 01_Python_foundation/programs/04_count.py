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
vowels = 'aeiou'
c_vowel = 0
c_const = 0
for i in user:
    if(i in vowels):
        c_vowel+=1
    elif(i == " "):
        pass
    else:
        c_const+=1
print("Vowel = ",c_vowel)
print("Consonant = ",c_const)