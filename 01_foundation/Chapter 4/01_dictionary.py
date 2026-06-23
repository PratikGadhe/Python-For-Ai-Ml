""" dictionary : Dictionaries are used to store data values in key:value pairs
They are unordered, mutable(changeable) & don't allow duplicate keys"""

dict={"Name":"Pratik Vilas Gadhe",
      "language":["C","Python"],
      "marks":(89,90),
      57 : "roll number"
      }
print(dict)
print(type(dict))

print(dict["Name"])
dict["Name"]="Pratik"
print(dict)
dict["surname"]="Gadhe"
print(dict)

dict1={

}
dict1["middle_name"]="vilas"
print(dict1)