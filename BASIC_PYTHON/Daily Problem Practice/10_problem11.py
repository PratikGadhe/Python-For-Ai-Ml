# Write a Python Program to Remove Punctuation From a String.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string=input("Enter string : ")
no_punct=""
for char in string:
    if char not in punctuations:
        no_punct+=char
print(no_punct)