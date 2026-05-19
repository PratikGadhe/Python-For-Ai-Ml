# Write a Python Program to find sum of array.
arr=[1,2,4,5,6,7,8,9,10]
def sum_of_array(arr):
    total=0
    # for i in range(1,len(arr)):
    #     total+=arr[i]
    for i in arr:
        total+=i
    return total
print(f"Sum of array : {sum_of_array(arr)}")
