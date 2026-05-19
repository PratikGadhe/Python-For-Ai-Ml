# Write a Python Program to calculate the natural logarithm of any number.
import math
n=float(input("Enter a number : "))
if(n<=0):
    print(f"Number should be positive")
else:
    print(f"Log of {n} is {round(math.log(n),2)}")