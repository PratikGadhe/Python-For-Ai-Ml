#1. str.endswith() function

name="Pratik Vilas Gadhe"
print(name.endswith("dhe"))

#2. str.capitalize() # capitalizes 1st char

str="i am learning python from apna college"
str1=str.capitalize()
# print(str1)

#3. str.replace( old, new ) #replaces all occurrences of old

str1="i am learning C programming from apna college"
str1=str1.replace("C","Python")
print(str1)

#4. str.find(word) #returns 1st index of 1st occurrer

str2="I am Gujarat"
str2=str2.find("am")
print(str2)

#5. str.count() function 

str3="I am from gujarat , and learning python from apna college"
print(str3.count("from"))
print(len(str3))