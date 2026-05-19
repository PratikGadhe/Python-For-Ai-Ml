# Write a Python Program to Find LCM.
# n=16,24 
n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))
def print_lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x == 0) and (greater%y == 0)):
            lcm = greater
            break
        greater+=1
    return lcm
x=print_lcm(n1,n2)
print(f"Lcm of {n1,n2} is {x}")