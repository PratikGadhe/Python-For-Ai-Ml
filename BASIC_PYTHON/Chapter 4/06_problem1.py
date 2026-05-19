"""
Store following word meanings in a python dictionary :
table: "a piece of furniture", "list of facts & figures" cat : "a small animal"
"""
dict={}
dict["table"]="A piece of furniture"
dict["List"]="List of facts and figures"
dict.update({"cat":"a small animal"})
print(dict)