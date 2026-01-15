#datatypes : Number , String , List , Tuple , disctionaries , sets
#1. Number : Integer and float
a = 5+10
print(a)
b=5.0+10.0
print(b)

#2.Strings
first_name="Pratik"
last_name="Gadhe"
full_name=first_name + " " + last_name #string manipulation
print(full_name)

long_dash = "-"
print(long_dash*10) #string replication

#length function
str="pratik gadhe"
print(len(str))

#3. Boolean
age = 20
has_license = True
can_drive = age>=18 and has_license

#fstring
name = "pratik"
print(f"My name is {name}")
#string methods
str="My name is pratik , name "
str.lower()
str.upper()
str.title()
str.capitalize()
str.startswith("My")
str.endswith("pratik")
str.find("pratik")
str.count("name")
str.replace("pratik","sanket")

#decision in python (if-else statements!)
temp = 31
if temp >= 32:
    print("Normal temperature")
elif temp >=39:
    print("its too hot!!!")
else:
    print("its nice weather")

#loop in python (for/while/do while loops!)

str ="pratik"
for i in str:
    print(i+str)

for i in range(10):
    print(i)

from math import sqrt,pi
sqrt(16)

import random 
number = random.randint(1,10)
print(number)