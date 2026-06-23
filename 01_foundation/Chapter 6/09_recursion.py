#Recursion : when a function call itself repeatedly is known as Recursion

def show(n):
    if(n==15):
        return
    print(n)
    show(n+1)

show(5)