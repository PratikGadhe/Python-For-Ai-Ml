# calculate the average of 3 numbers

def average(a,b,c):
    average=(a+b+c)/3
    return average

x=int(input("Enter number : "))
y=int(input("Enter number : "))
z=int(input("Enter number : "))

output=average(x,y,z)
print("Average is ",output)