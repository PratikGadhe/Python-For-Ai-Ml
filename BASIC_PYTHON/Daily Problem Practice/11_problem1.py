# Write a Python program to print all disarium numbers between 1 to 100.
n=int(input("Enter range : "))
# list=[]
# for i in range(1,n+1):
#     temp=i
#     length=len(str(i))
#     total=0
#     while(temp>0):
#         digit=temp%10
#         total+=digit**length
#         temp//=10
#         length-=1
#     if(total == i):
#         list.append(i)
# print(list)
for i in range(1,n+1):
    count=1
    total=0
    for j in str(i):
        total+=int(j)**count
        count+=1
    if(total == i):
        print (i,end=" ")
print("\n")