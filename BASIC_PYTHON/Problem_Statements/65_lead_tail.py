"""
65. Remove Leading and Trailing Spaces
Problem Statement:
Write a program to remove leading and trailing spaces from a string without using built-in
strip().
Input:
 A string
Output:
 Trimmed string
Example:
Input: " hello "
Output: "hello"
"""
s = " hello "

start = 0
end = len(s) - 1

# Remove leading spaces
while start <= end and s[start] == ' ':
    start += 1

# Remove trailing spaces
while end >= start and s[end] == ' ':
    end -= 1

result = ""

for i in range(start, end + 1):
    result += s[i]

print(result)