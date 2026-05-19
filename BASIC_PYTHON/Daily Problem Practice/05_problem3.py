#Write a Python Program to Display factorial Using Recursion.
n=int(input("Enter a Number : "))
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else :
        return n*factorial(n-1)
    
print(f"Factorial of {n} is {factorial(n)}")