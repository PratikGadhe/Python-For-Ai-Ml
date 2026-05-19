"""
Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
x=int(input("Enter a number : "))
tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
idx=0
for i in tuple :
    if(x == i):
        print("Number found at index",idx)
        break
    idx+=1
    