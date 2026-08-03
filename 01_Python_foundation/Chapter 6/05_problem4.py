# WAF to find the factorial of n. (n is the parameter)
n=int(input("Enter a number : "))
def factorial(a):
    fact=1
    for i in range(1,n+1):
        fact=fact*i 
    return fact

fact=factorial(n)
print("Factorial of",n,"is",fact)