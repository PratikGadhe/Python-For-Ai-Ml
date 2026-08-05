# Write a Python Program to Check if a Number is Odd or Even.
n = int(input("Enter a number : "))
if(n%2 == 0):
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")

# Write a Python Program to Check Leap Year.
n = int(input("Enter a year : "))
if(n % 4 == 0 and n % 100 != 0):
    print(f"{n} is a leap year")
elif(n % 400 == 0 and n % 100 == 0):
    print(f"{n} is a leap year and centurian year too")
else:
    print(f"{n} is not a leap year")

# Write a Python Program to Check Prime Number.
n = int(input("Enter a number : "))
prime = True
for i in range(2,n):
    if(n%i != 0):
        prime = True
    else:
        prime = False
        break
if(prime):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not prime number")

# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# print("prime number between 1-10 are : ")
for i in range(1,10):
    for j in range(2,i):
        prime = 1
        if(i % j != 0):
            prime = 1
        else : 
            prime = 0
            break
    if(prime == 1):
        print(i)

# Write a Python Program to Find the Factorial of a Number.
n = int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f'factorial of {n} is {fact}')

# Write a Python Program to Print the Fibonacci sequence.
fib0 = 0
fib1 = 1
print(fib0 , fib1 , ", ")
for i in range(2,10):
    fib = fib0 + fib1
    print(fib)
    fib0,fib1 = fib1,fib

# Write a Python Program to Check Armstrong Number?
n = int(input("Enter a number : "))
power = len(str(n))
result = 0
for i in str(n):
    result += (int(i)**power)
if (result == n):
    print(f"{n} is an armstrong number")
else: 
    print(f"{n} is not an armstrong number")

# Write a Python Program to Find Armstrong Number in an Interval.
n = int(input("Enter a range : "))
for i in range(1,n+1):
    power = len(str(i))
    result = 0
    for j in str(i):
        result += int(j)**power
    if(result == i):
        print(result)
