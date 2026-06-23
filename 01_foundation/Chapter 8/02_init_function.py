# Constructor : All classes have a function called _init_O, which is always executed when the class is being initiated.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
name1="pratik"
marks1=[70,80,90]

name2="Sanket"
marks2=[80,90,60]

s1=Student(name1,marks1)
s2=Student(name2,marks2)

print(f"Name of student 1: {s1.name}\nMarks of student1 : {s1.marks}")
print(f"Name of student 2: {s2.name}\nMarks of student1 : {s2.marks}")