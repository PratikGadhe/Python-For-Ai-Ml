# Write a recursive function to calculate the sum of first n natural numbers.
n=int(input("Enter a number : "))

def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)

print(f"sum of {n} is {sum(n)}")