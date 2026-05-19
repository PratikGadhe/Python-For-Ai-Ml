# Write a Python program to determine whether the given number is a Harshad Number.
"""
18 is a Harshad number because 1+8 = 9 and 18 is divisble by 9
42 is not a Harshad number 

"""
# n=int(input("Enter a number : "))
# sum=0
# for i in str(n):
#     sum+=int(i)
# if(n % sum == 0):
#     print(f"{n} is harshad number")
# else:
#     print(f"{n} is not harshad number")
n = int(input("Enter a number: "))
digit_sum = 0
for i in str(n):
    digit_sum += int(i)

if n % digit_sum == 0:
    print(f"{n} is a Harshad number")
else:
    print(f"{n} is not a Harshad number")
