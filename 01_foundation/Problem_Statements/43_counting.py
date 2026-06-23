"""
43. Count Lines, Words, Characters
Problem Statement:
Write a program to count lines, words, and characters in a text.
Input:
 Multi-line string
Output:
 Line count, word count, character count
Example:
Input: "Hello\nWorld"
Output: Lines = 2, Words = 2, Characters = 10
"""
text = "Hello\nWorld"

lines = text.split('\n')
words = text.split()

line_count = len(lines)
word_count = len(words)
char_count = len(text)

print("Lines =", line_count)
print("Words =", word_count)
print("Characters =", char_count)