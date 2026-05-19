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

def reverse(str):
    n = len(str)-1
    if(n<0):
        return ""
    else:
        return str[n] + reverse(str[0:n])
result = reverse(string)
print(result)