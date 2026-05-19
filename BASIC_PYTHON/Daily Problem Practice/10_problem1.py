# Write a Python Program to Split the array and add the first part to the end?
arr=[1,2,3,4,5]
length=int(len(arr)/2)

def split_array(arr,length):
    first_part=arr[:length]
    second_part=arr[length:]
    result=second_part+first_part
    return result
    # for i in range(length,len(n)):
    #     list.append(n[i])
    # for i in range(0,length):
    #     list.append(n[i])
print(f"Original array : {arr}")
print(f"After Spliting : {split_array(arr,length)}")