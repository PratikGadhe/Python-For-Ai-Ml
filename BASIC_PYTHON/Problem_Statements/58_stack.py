"""
58. Check Balanced Parentheses
Problem Statement:
Create a program to check if parentheses are balanced.
Input:
 String
Output:
 True / False
Example:
Input: "(())"
Output: True
"""
s = "(())"

stack = []
balanced = True

for ch in s:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if len(stack) == 0:
            balanced = False
            break
        stack.pop()

if len(stack) != 0:
    balanced = False

print(balanced)