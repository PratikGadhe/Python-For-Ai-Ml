"""
4. Remove All Occurrences of a Word
Problem Statement:
Write a program to remove all occurrences of a specified word from a list of words.
Input:
 List of words
 Word to remove
Output:
 Updated list
Example:
Input: ["apple", "banana", "apple", "cherry"], remove "apple"
Output: ["banana", "cherry"]
"""
list = ["apple", "banana", "apple", "cherry"]
user = input("Enter a word to be removed : ")
final = []
for i in list:
    if(i != user):
        final.append(i)
print(final)