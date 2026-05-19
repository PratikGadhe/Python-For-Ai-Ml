# class attribute are basically of two types : 1. data , 2. method
class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def name1(self):
        return self.name
    def marks(self):
        return self.marks


s1=Student("Pratik",[70,80,90])
print(s1.name1())