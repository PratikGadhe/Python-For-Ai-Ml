"""
20. Split String into Words and Count Length
Problem Statement:
Write a program to split a sentence into words and display each word along with its length.
Input:
 A string sentence
Output:
 Words with their respective lengths
Example:
Input: "Python is fun"
Output: Python–6, is–2, fun–3
"""
string = "Python is fun"
l1 = string.split()
for i in l1:
    length = len(i)
    print(i,"-",length)