# Write a Python program to print all disarium numbers between 1 to 100.
import my_module
n=int(input("Enter range : "))
# print(my_module.dis_range(n))
print(my_module.dis_range.__doc__)
for i in range(1,n+1):
    initial=1
    num=0
    for j in str(i):
        num+=int(j)**initial
        initial+=1
    if(num == i):
        print(i,end=" ")
print("\n")
