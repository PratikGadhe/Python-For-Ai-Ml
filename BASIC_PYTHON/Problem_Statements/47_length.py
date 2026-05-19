"""
47. Find Length of String Using Recursion
Problem Statement:
Write a recursive function to find the length of a string.
Input:
 String
Output:
 Length
Example:
Input: "abc"
Output: 3
"""
def string_length(s):
    # Base case
    if s == "":
        return 0
    # Recursive case
    return 1 + string_length(s[1:])

# Input
text = "abc"

# Output
print(string_length(text))