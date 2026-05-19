def disarium(n):
    j=1
    num=0
    for i in str(n):
        num+=int(i)**j
        j+=1
    if n==num:
        return True
    else:
        return False
def dis_range(n):
    '''this will print Disarium number'''
    for i in range(1,n+1):
        initial=1
        num=0
        for j in str(i):
            num+=int(j)**initial
            initial+=1
        if(num == i):
            print(i,end=" ")
    print("\n")