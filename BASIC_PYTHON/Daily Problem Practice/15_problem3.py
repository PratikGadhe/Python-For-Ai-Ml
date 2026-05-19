
# Write a Python program to print all harshad numbers between 1 and 100.

n=int(input("Enter range : "))
for i in range(1,n+1):
    sum=0
    for j in str(i):
        sum+=int(j)
    if(i % sum == 0):
        print(i,end=" ")
print("\n")