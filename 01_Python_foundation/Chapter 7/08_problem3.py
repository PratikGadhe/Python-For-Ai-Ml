# Search if the word "learning" exists in the file or not.
word="xlearning"
with open("/Users/pratikvilasgadhe/Desktop/Programming/BASIC_PYTHON/practice.txt","r") as f:
    data=f.read()
    if(data.find(word) >= 0):
        print("Word found !")
    else:
        print("Not found !")