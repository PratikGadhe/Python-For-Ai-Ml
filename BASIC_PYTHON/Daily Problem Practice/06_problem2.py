# Program to the maximum in an array.
arr=[1,5,2,3,9,0,10]
greater=arr[0]
for i in arr:
    if(i > greater):
        greater=i
# for i in range(1,len(arr)):
#     if(arr[i] > greater):
#         greater=arr[i]
print(f"Maximum number is {greater}")