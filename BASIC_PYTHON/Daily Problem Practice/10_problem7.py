# Write a Python program to print even and odd numbers in a list.
list=[2,4,6,1,2,3,5,8,7,9,10]
even=[]
odd=[]
# def even_number(list,even):
#     for i in list:
#         if(i%2 == 0):
#             even.append(i)
#     return even
# def odd_number(list,odd):
#     for i in list:
#         if(i%2 != 0):
#             odd.append(i)
#     return odd
# print(f"Even numbers is list are {even_number(list,even)}")
# print(f"Odd numbers is list are {odd_number(list,odd)}")
# e=[num for num in list if(num%2 == 0)]
# print(e)
def even_odd(list):
    even=[]
    odd=[]
    for i in list :
        if(i%2 == 0):
            even.append(i)
        else:
            odd.append(i)
    return even,odd
even_numbers, odd_numbers = even_odd(list)
print(f"Even numbers is list are {even_odd(even_numbers)}")
print(f"Odd numbers is list are {even_odd(odd_numbers)}")