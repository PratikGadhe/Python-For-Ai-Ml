from matplotlib import pyplot as plt
#syntax : plt.plot(x-axis , y-axis)
"""
Markers Availabe: 
1. dot (.) : point
2. start (*) : star
3. D : Diamond
4. o : big point
5. v : down_triangle
6. s : square
7. p : pentagon and more...
"""
section = ['A','B','C','D']
students = [10,20,15,30]
plt.figure(figsize = (10,5))
plt.grid(True)
plt.xlabel("Sections")
plt.ylabel("Students")
plt.title("Section wise students strength")
plt.plot(section,students,color = 'red',marker = '*')
plt.yticks(students)
plt.show()