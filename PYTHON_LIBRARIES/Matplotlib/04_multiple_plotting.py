import matplotlib.pyplot as plt
x1 = [10,20,30,45,50]
y1 = [15,20,25,30,40]
x2 = [10,20,30]
y2 = [10,15,30]
plt.plot(x1,y1,color='black',marker = "*",label = "First Line")
plt.plot(x2,y2,color="red",marker = 'D',label = "Second Line")
plt.title("Multiple plotting")
plt.xlabel("x1 x2")
plt.ylabel("y1 y2")
plt.grid(True)
plt.legend()
plt.show()