# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
name=input("Enter Student Name : ")
m1=int(input("Enter Marks 1 : "))
m2=int(input("Enter Marks 2 : "))
m3=int(input("Enter marks 3 : "))
marks=[m1,m2,m3]
class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=(marks[0]+marks[1]+marks[2])
    def average(self):
        average=self.marks/3
        return average
    
s1=Student(name,marks)
print(f"Name of student : {s1.name}")
print(f"Average of Student 1 is {s1.average()}%")