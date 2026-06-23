"""
15. Recursive Reverse String
Problem Statement:
Develop a recursive function to reverse a given string.
Input:
 String
Output:
 Reversed string
Example:
Input: "hello"
Output: "olleh"
"""
string = "hello"
def reverse(string):
    n = len(string)-1
    if(n<0):
        return ""
    else:
        return string[n]+reverse(string[:n])
print(reverse(string))