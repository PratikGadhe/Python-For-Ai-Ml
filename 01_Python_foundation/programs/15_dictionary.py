"""
21. Create Dictionary from String Characters
Problem Statement:
Develop a program to create a dictionary where keys are characters and values are their
frequencies in a string.
Input:
 A string
Output:
 Dictionary of character frequencies
Example:
Input: "apple"
Output: {'a':1, 'p':2, 'l':1, 'e':1}
"""
string = 'apple'
dict = {}
for i in string:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)