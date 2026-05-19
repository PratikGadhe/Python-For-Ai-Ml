# Write a Python program to find largest number in a list
list=[10,100,21,81,0,-1,1000]
largest=list[0]
def largest_number(list,largest):
    for i in list:
        if(i>largest):
            largest=i
    return largest
print(f"Largest number in list : {largest_number(list,largest)}")