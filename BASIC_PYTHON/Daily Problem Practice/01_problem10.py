# Write a Python Program to Check if a Number is Positive, Negative or Zero.
number=int(input("Enter a Number : "))
if(number>0):
    print(f"{number} is positive ")
elif(number == 0):
    print(f"{number} is neither positive nor negative ")
else:
    print(f"{number} is negative ")