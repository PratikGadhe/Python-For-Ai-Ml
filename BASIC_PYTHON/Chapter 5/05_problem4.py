"""
Search for a number x in this tuple using loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
"""
tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=int(input("Enter a number : "))
i=0
while(i<len(tuple)):
    if(x == tuple[i]):
        print("Number",x,"is present at index",i)
        break
    i+=1
