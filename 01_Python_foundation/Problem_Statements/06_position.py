"""
6. Find Substring Positions
Problem Statement:
Write a program to find all occurrences and positions of a substring within a given string.
Input:
 Main string
 Substring
Output:
 List of starting indices where substring occurs
Example:
Input: String = "banana", Substring = "ana"
Output: [1, 3]
"""
String = "banana"
Substring = "ana"
final = [String.find(Substring),len(Substring)]
print(final)
      