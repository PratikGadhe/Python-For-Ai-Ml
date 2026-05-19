# Write a Python program to Multiply all numbers in the list.
l=[1,2,3,4,5]
pro=1
def product(l,pro):
    for i in l:
        pro *= i
    return pro
print(f"Product of all number in matrix is {product(l,pro)}")