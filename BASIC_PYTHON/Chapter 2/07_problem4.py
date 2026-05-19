#WAP to find the greatest of 3 numbers entered by the user.
n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
n3=int(input("Enter Number 3 : "))

if(n1>n2 and n1>n3):
    print(n1,"is a greatest number")
elif(n2>n1 and n2>n3):
    print(n2,"is a greatest number")
else:
    print(n3,"is a greatest number")