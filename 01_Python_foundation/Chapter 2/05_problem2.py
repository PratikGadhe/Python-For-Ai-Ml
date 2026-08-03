"""
Grade students based on marks
marks >= 90, grade = "A"
90 > marks »= 80, grade = "B"
80 > marks »= 70, grade = "C"
70 > marks, grade = "D"

"""
marks=int(input("Enter Your marks : "))
if(marks >= 90 and marks <= 100):
    print("Grade : A ")
elif(marks >= 80 and marks < 90):
    print("Grade : B")
elif(marks >=70 and marks < 80):
    print("Grade : C")
else:
    print("Grade : D")