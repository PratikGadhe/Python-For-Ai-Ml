"""
wap to remove the ith occurrence from a list of element 
"""

n = ["apple","banana","cherry","apple"]
lst = []
count = 0
word = input("Enter a element to be removed : ")
occurrence = int(input("Enter the occurrence to be removed : "))
for i in n:
    if(i == word):
        count = count + 1
        if(count != occurrence):
            lst.append(i)
    else:
        lst.append(i)
if(count == 0):
    print("Element not found!!")
else:
    print(f"Number of repetition for removed word ({word}): ",count)
    print("Updated List : ",lst)
    print("Distinct element : ",set(n))

