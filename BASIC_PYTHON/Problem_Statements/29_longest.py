"""
29. Find Longest Word in a Sentence
Problem Statement:
Create a program to find the longest word in a given sentence.
Input:
 A string sentence
Output:
 Longest word
Example:
Input: "Machine learning is powerful"
Output: "learning"
"""
string = "Machine learning is powerful"

words = string.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)