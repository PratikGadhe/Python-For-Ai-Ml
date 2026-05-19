# Write a Python program to find smallest number in a list.
l=[-1,2,3,4,0,-9,10]
smallest=l[0]
def smallest_number(l,smallest):
    for i in l:
        if ( i < smallest):
            smallest=i
    return smallest
print(f"Smallest number : {smallest_number(l,smallest)}")