# file I/O 
f=open("/Users/pratikvilasgadhe/Desktop/Programming/BASIC_PYTHON/Chapter 7/sample.txt","r")
data=f.read()
print(data)
print(len(data))
f.close()