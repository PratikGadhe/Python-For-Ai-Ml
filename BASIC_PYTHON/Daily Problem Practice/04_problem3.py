# Write a Python Program to Find HCF.
n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))
def print_hcf(x,y):
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range (1,smaller+1):
        if((x%i == 0) and (y%i == 0)):
            hcf=i
    return hcf
print(f"HCF of {n1,n2} is {print_hcf(n1,n2)}")