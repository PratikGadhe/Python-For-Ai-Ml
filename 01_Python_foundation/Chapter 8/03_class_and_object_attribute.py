# there are two attributes 1. class attribute and 2. object attribute

class Student:
    college_name="Svkm IoT College , Dhule" #this is class attribute
    branch="Computer"
    def __init__(self,name,prn,marks,average):
        self.name=name  #this is object attribute
        self.prn=prn
        self.marks=marks
        self.average=average

name1="Pratik Gadhe"
prn1=24054491245048
marks1=[70,80,90]
average1=(marks1[0]+marks1[1]+marks1[2])/3

name2="Prathamesh Dixit"
prn2=24054491245047
marks2=[80,60,70]
average2=(marks2[0]+marks2[1]+marks2[2])/3

s1=Student(name1,prn1,marks1,average1)
s2=Student(name2,prn2,marks2,average2)

print(f"Name of College : {s1.college_name}")
print(f"Name of Student : {s1.name}")
print(f"Prn of student : {s1.prn}")
print(f"Average Marks of student : {s1.average}")