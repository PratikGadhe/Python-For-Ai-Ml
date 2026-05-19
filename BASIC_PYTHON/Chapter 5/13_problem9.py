# WAP to find the sum of first n numbers. (using while)

n = int (input("Enter a number : "))
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print("sum of n natural numbers are ",sum)

# WAP to find the sum of first n numbers. (using for loop)
n=int ( input ( "Enter a number : "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of ",n," natural number :",sum)