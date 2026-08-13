# multiple plotting
import matplotlib.pyplot as plt
x1 = [10,20,30,45,50]
y1 = [15,20,25,30,40]
x2 = [10,20,30]
y2 = [10,15,30]
x3 = [12,24,19,25]
y3 = [24,48,27,36]
plt.plot(x1,y1,color='black',marker = "*",label = "First Line")
plt.plot(x2,y2,color="red",marker = 'D',label = "Second Line")
plt.plot(x3,y3,color="blue",marker = '.',label = "Third Line")

plt.title("Multiple plotting")
plt.xlabel("x1 x2 x3")
plt.ylabel("y1 y2 y3")
plt.grid(True)
plt.legend()
plt.show()