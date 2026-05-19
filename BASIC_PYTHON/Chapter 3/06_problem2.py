#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
list=[1,2,3,2,1]
list1=list.copy()
list1.reverse()
if(list==list1):
    print("list is a palindrome")
else:
    print("List is not a palindrome")