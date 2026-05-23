from matplotlib import pyplot as plt
import numpy as np
objects = ['Python','C++','Java','perl','Scala','Lisp']
y_axis = np.arange(1,len(objects)+1)
performance = [10,8,6,4,2,1]
plt.barh(y_axis,performance,align = 'center', color = 'blue')
# plt.xticks(x_axis)
plt.title("Horizontal")
plt.xlabel("list")
plt.ylabel('Numpy')
# plt.yticks(y_axis)
# plt.grid(True)
plt.show()