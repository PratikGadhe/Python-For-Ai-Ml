"""list : A built-in data type that stores set of values
It can store elements of different types (integer, float, string, etc.)"""

#important point : list are MUTABLE (whose value can be change) and String are IMMUTABLE (whose values cannot be change)
marks=["pratik",20,99.5]
print(type(marks))
print(len(marks))
print(marks)

#mutable example
marks[0]="Sanket"
marks[1]=23
print(marks)

#indexing in list
marks1=[90,80,70,60,50,40,30,20,10]
print(marks1[0:6])
#negative indexing
print(marks1[-5:-1])#[4:8]