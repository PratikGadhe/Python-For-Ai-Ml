from matplotlib import pyplot as plt
y_axis = [10,20,30,40]
x_axis = range(len(y_axis))
plt.bar(x_axis , y_axis , width = 0.5 , color = 'cyan',label = "Cyan Color")
plt.xticks(x_axis)
plt.title("Foundation of Barchart")
plt.xlabel("X - axis")
plt.ylabel('Y - axis')
# plt.yticks(y_axis)
# plt.grid(True)
plt.legend()
plt.show()