# Write a Python Program to Remove Punctuation From a String.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
punct=""
sentence=input("Enter a string : ")
for i in sentence:
    if i not in punctuations:
        punct=punct+i
print(punct)