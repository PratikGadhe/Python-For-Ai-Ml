"""
19. Check Anagram Strings
Problem Statement:
Create a program to check whether two strings are anagrams of each other.
Input:
 Two strings
Output:
 True / False
Example:
Input: "listen", "silent"
Output: True
"""
n1 = "listen"
n2 = "silent"

if(sorted(n1) == sorted(n2)):
    print(True)
else:
    print(False)
