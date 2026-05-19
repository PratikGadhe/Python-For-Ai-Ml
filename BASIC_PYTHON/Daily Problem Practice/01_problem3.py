# Write a Python program to swap two variables
n1=int(input("Enter a number 1 : "))
n2=int(input("Enter a number 2 : "))
print(f"Numbers before swapping : a={n1} and b={n2}")
# temp=n1
# n1=n2
# n2=temp
n1,n2=n2,n1
print(f"Numbers after swapping : a={n1} and b={n2}")