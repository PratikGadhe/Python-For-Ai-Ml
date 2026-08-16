import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [1,9,21,31,41,51]
plt.hist(data,bins=[0,10,20,30,40,50,60],
         facecolor = 'cyan',edgecolor = 'black')
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("frequency")
plt.savefig("student.png")
plt.show()