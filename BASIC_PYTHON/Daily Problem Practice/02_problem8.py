# Write a Python Program to Check Armstrong Number?
#153 is armstrong : 1^3+5^3+3^3=153

n=input("Enter a number : ")
# str_num=len(str(n))
length=len(n)
total=0
# temp=n
"""
while(temp>0):
    num = temp%10 #store the last digit
    total+=num**str_num
    temp//=10 #remove the last digit
"""
for i in n:
    total+=int(i)**length
if(n == total):
    print(f"{n} is a Armstrong Number ")
else:
    print(f"{n} is not a Armstrong Number ")