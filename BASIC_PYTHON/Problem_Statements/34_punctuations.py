"""
34. Remove Punctuation from String
Problem Statement:
Create a program to remove all punctuation marks from a given string.
Input:
 A string
Output:
 String without punctuation
Example:
Input: "Hello, World!"
Output: "Hello World"
"""
string = "Hello, World!"
result = ""
for i in string:
    if(i not in ".,?!;'-_|(){}"):
        result+=i
print(result)