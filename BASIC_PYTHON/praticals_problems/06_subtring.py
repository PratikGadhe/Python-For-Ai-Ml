"""
wap to find if given substring is present in a string
"""
# 1. IN operator
string = "I am Pratik Vilas Gadhe"
sub_str = "Pratik"
if(sub_str in string):
    print(f"Yes '{sub_str}' is in the string")
else:
    print(f"No, '{sub_str}' not in a string")

# split() method
string = "I am Pratik Vilas Gadhe"
sub_str = "Pratik"
lst = string.split()
for i in lst:
    if(i == sub_str):
        check = True
        break
    else:
        check = False
if(check):
    print(True)
else:
    print(False)

# 3. find() method
string = "I am Pratik Vilas Gadhe"
sub_str = "Pratik"
if(string.find(sub_str) != -1):
    print("yes it is present in a string")
else:
    print("no")

string = "I am Pratik Vilas Gadhe"
sub_str = "Pratik"
if(string.count(sub_str) > 0):
    print("yes it is present in a string")
else:
    print("no")