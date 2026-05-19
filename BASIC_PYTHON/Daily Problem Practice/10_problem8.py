# Write a Python Program to Sort Words in Alphabetic Order.
name=input("Enter names : ")
# words=[word.capitalize() for word in name.split()]
# words.sort()
# for word in words:
#     print(word)
list=name.split()
list.sort(key=str.lower)
for i in list:
    print(i)