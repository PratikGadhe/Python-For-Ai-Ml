"""
9. Dictionary Based on Word Length
Problem Statement:
Create a dictionary where the key represents the length of words and the value is a list of
words having that length.
Input:
 List of words
Output:
 Dictionary grouping words by length
Example:
Input: ["hi", "hello", "cat"]
Output: {2: ["hi"], 3: ["cat"], 5: ["hello"]}
"""
input = ["hi", "hello", "cat"]
dict = {}
count = 0
for i in input:
    count = len(i)
    dict[count] = i
print(dict)