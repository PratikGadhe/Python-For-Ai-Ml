# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
n=int(input("Enter Range : "))
prime = 1
print(f"Prime number between (1-{n}) are ",end=": ")
for i in range(2,n):
    for j in range(2,i):
        if(i%j != 0):
            prime = 1
        else:
            prime = 0
            break
    if(prime == 1):
        print(i,end=" , ")
print("\n")
