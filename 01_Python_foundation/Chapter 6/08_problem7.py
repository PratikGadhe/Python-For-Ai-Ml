# waf to swap to numbers 
n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
def swap(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)

swap(n1,n2)