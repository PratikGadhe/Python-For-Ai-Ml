# Write a Python program to check if the given number is a Disarium Number.
"""
A Disarium number is a number that is equal to the sum of its digits each raised to the power of its respective position.
For example, 89 is a Disarium number because
8^1+9^2=89
"""
num = int(input("Enter a number : "))
count=1
total=0
for i in str(num):
    total+=int(i)**count
    count+=1
if num == total:
    print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")
# temp = num

# Find number of digits
# length = len(str(num))

# sum_digits = 0

# while temp > 0:
#     digit = temp % 10
#     sum_digits += digit ** length
#     temp //= 10
#     length -= 1  # decrease position from right to left

# if sum_digits == num:
#     print(f"{num} is a Disarium number")
# else:
#     print(f"{num} is not a Disarium number")