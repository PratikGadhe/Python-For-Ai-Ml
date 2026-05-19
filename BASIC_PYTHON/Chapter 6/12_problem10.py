# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

list=[1,2,3,4,5,6,7,8,9]
def element (list,idx):
    if(idx == len(list)):
        return 
    print(list[idx])
    element(list,idx+1)
element(list,0)