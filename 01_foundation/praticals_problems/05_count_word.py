"""
wap to count the frequency of word appearing in a string using dictionary
"""

# using dictionary
n = "apple apple banana cherry mango"
lst = n.split()
dict1 = {}
for i in lst:
    if(i in dict1):
        dict1[i]+=1
    else:
        dict1[i] = 1
print(dict1)

# 2. string 
n = "apple apple banana cherry mango"
word = ""
dict1 = {}
for i in n:
    if(i != " "):
        word += i
    else :
        if(word in dict1):
            dict1[word] +=1
        else :
            dict1[word] = 1
        word = ""
print(dict1)


# # from collection import counter
# n = "apple apple banana cherry mango"
# def word_counter(n):
#     # lst = n.split()
#     # return counter(lst)
# print(word_counter(n))