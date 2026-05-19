# Write a Python program to find N largest elements from a list.
n=int(input("Enter n :"))
list=[1,4,8,0,10,100,1001,11,111,123]
def n_largest_number(list,n):
    list.sort(reverse=True)
    return list[n-1]
print(f"{n} largest number in list is {n_largest_number(list,n)}")
