# Methods that don't use the self parameter (work at class level) are called as static method
class Student :
    @staticmethod
    def hello():
        print("Hello")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Pratik",[70,80,90])
s1.hello()