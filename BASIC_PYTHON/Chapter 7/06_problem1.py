"""
Create a new file "practice.txt" using python. Add the following data in it:
Hi evervone
we are learning File I/O using Java.
I like programming in Java.
"""
f=open("practice.txt","w")
f.write("Hi everyone\n")
f.write("we are learning file I/O using Java\n")
f.write("I like Programming in java")
f.close()