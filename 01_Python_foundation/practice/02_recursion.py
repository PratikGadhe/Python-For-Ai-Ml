# Write a Python Program to Find Factorial of Number Using Recursion.
n = int(input("Enter a number : "))

def factorial(n):
    if(n<=1):
        return 1
    return n * factorial(n-1)

result = factorial(n)
print(f"{result} is a factorial result of {n}")

# Write a Python Program to Display Fibonacci Sequence Using Recursion.

n = int(input("Enter a range :"))

def fibonacci(n):
    if n <= 1 :
        return n
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(n):
    print(fibonacci(i))