
import matplotlib.pyplot as plt
def fnplot(student , marks):
    plt.plot(student,marks,color = "red",marker = "*",label = "Students")
    plt.title("Student vs Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.xticks(student)
    plt.yticks(marks)
    plt.legend()
    plt.show()
stud = [1,2,3,4,5,6,7,8,9,10]
marks = [50,65,75,80,82,90,47,81,63,62]
fnplot(stud,marks)