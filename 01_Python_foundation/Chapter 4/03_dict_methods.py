#method of dictionary
#1. dict.keys(): returns all keys
dict={"Name":"Pratik vilas gadhe","language":"python","marks":96.5,"roll_number":57}
# print(dict.keys())

#2. dict.values() : returns all values
# print(dict.values())
# print(list(dict.keys()))
# print(tuple(dict.values()))

#3. myDict.items() : #returns all (key, val) pairs as tuples

# print(dict.items())
pair=list(dict.items())
# print(pair[0])

#4. dict.get("key") :

# print(dict["Name"]) #return value
# print(dict.get("Name")) #return value

# but both have some minorr difference like..
# print(dict["Name2"])    #it will give error !
print(dict.get("Name2"))    #it will not give error thats the difference

#5. dict.update() : insert specified items in dictionary

dict2={"cgpa":8.79,"prn":24054491245048,"Name":"Sanket Vilas Gadhe"}
dict.update(dict2)
print(dict)
