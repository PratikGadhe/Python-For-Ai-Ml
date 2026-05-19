"""
8. Most Frequent Word
Problem Statement:
Write a program to identify the most frequently occurring word in a given string.
Input:
 A string
Output:
 Word with highest frequency
Example:
Input: "cat dog cat bird dog cat"
Output: cat
"""
text = "cat dog cat bird dog cat"
words = text.split()

max_count = 0
most_word = ""

for i in range(len(words)):
    count = 0
    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1
    
    if count > max_count:
        max_count = count
        most_word = words[i]

print(most_word)