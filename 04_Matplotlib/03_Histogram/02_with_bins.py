import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
std = [19,25,30,35,25,60]
plt.hist(std,bins = [0,10,20,30,40,50,60],
        edgecolor = 'red',facecolor = 'y')
plt.show()