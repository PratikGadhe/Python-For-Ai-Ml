# From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("/Users/pratikvilasgadhe/Desktop/Programming/BASIC_PYTHON/Chapter 7/sample.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    for value in nums:
        if(int(value)%2 == 0):
            count+=1
print(count)