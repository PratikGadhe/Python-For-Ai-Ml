import numpy as np
import matplotlib.pyplot as plt
arr1 = np.arange(1,11)
arr2 = [1,2,3,4,5,6,7,8,9,10]
arr3 = [4,5,6,7,8,9,10,11,12,13]
plt.title("Graph One")
plt.subplot(2,1,1)
plt.plot(arr1,arr2,color = "red")
plt.grid(True)
plt.subplots_adjust(hspace = 0.4 ,wspace = 0.4)
plt.subplot(2,1,2)
plt.title("Graph Two")
plt.plot(arr1,arr3,color = 'black')
plt.grid(True)
plt.show()
