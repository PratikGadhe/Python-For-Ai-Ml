# Write a Python Program for cube sum of first n natural numbers?
n=int(input("Enter a number : "))
def cube_sum(n):
    total = 0
    if(n<=0):
        return 0
    else:
        for i in range(1,n+1):
            total+=(i**3)
        return total
if(n<=0):
    print("Please Enter Positive number ")
else:
    print(f"Cube Sum of {n} natural number is {cube_sum(n)}")
        
    