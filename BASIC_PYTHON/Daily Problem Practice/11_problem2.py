# Write a Python program to check if the given number is Happy Number.
# 19 is happy number
n = int(input("Enter a number: "))
original = n
seen = set()  # store sums we have seen

while n != 1 and n not in seen:
    seen.add(n)
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** 2
        temp //= 10
    n = total

if n == 1:
    print(f"{original} is a Happy Number")
else:
    print(f"{original} is not a Happy Number")
