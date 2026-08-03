#function : it is a block of code that performs specific task

#function definition :
def cal_sum(x,y): #where x,y are parameters 
    sum=x+y
    return sum 
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

#function call
sum=cal_sum(a,b) #where a,b are arguments 
print("Sum is ",sum)