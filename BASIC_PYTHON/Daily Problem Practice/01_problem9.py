# Write a Python program to swap two variables without temp variable.
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
a,b=b,a
print(f"after swapping a={a} and b={b}")