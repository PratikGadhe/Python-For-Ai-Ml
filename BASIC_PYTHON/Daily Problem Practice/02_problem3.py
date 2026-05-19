# Write a Python Program to Check Prime Number.
n=int(input("Enter a number : "))
for i in range(2,n):
    if(n%i != 0):
        prime = 1
    else:
        prime = 0
        break
if(prime == 1):
    print(f"{n} is a prime number !")
else:
    print(f"{n} is not a prime number !")