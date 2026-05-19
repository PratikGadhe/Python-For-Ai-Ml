# Write a Python program to check if the given number is Happy Number.
"""
Happy Number: A Happy Number is a positive integer that, when you repeatedly replace the number by the sum of the squares of its digits and continue the process, eventually reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number is not a Happy Number.
For example:
19 is a Happy Number because:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
"""
n=int(input("Enter a number : "))
total=0
temp=n
while(temp>0):
    num=temp%10
    total+=num**2
    num//10

if(total==1):
    print("yes")

else:
    print("no")