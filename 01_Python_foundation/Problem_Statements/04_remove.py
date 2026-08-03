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
word = input("Enter words by giving space : ").split()
remove = input("Enter a word to remove from list : ")
update = [ i for i in word if i!=remove]
print(update)
# another method
final = []
for i in word :
    if i != remove:
        final.append(i)
print(final)