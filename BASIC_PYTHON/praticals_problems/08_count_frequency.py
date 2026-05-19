"""
wap to count frequency of word appearing in a string
"""

# 1. count method
string = "the quick fox jumps over the sky"
sub_str = "fox"
counts = string.count(sub_str)
if (sub_str in string):
    print(counts)
else:
    print("substring is not in a string!!!")

# 2. using dictionary
string = "the quick fox jumps over the sky"
sub_str = "fox"
dict1 = {}
lst = string.split()
for key in lst:
    if(key in dict1):
        dict1[key]+=1
    else:
        dict1[key]=1
if(sub_str in dict1):
    print(dict1[sub_str])
else:
    print("Substring is not in string!!!")