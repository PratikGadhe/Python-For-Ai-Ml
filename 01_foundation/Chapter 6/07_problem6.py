# Waf to find the number n is even or odd 
n=int(input("Enter a number : "))
def check(n):
    if(n%2 == 0):
        print(n,"is Even")
    else:
        print(n,"is Odd")

check(n)