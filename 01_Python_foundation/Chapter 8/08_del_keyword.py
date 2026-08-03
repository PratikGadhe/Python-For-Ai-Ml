class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Pratik",90)
print(s1.name)
del s1.name
del s1
print(s1.marks)
print(s1.name)