import numpy as np
import matplotlib.pyplot as plt
x_value = np.arange(-2,1,0.01)
y_value = np.sin(x_value)
plt.plot(x_value,y_value)
plt.grid(True)
plt.show()