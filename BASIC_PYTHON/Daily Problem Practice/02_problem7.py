# Write a Python Program to Print the Fibonacci sequence.
n=int(input("Enter a number : "))
fib1=0
fib2=1
print("Fibonnacci Series :",end=" ")
print(fib1,fib2,end=" ")
for i in range(2,n):
    fibonacci=fib1+fib2
    print(fibonacci,end=" ")
    # fib1=fib2
    # fib2=fibonacci
    fib1,fib2=fib2,fibonacci
print("\n")
