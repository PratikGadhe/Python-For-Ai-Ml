"""
33. Count Words in a Sentence
Problem Statement:
Write a program to count the total number of words in a sentence.
Input:
 A string
Output:
 Number of words
Example:
Input: "Python is easy"
Output: 3
"""
string = "python is easy"
split = string.split()
print("number of words : ",len(split))