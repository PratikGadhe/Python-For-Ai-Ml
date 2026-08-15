import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame({"2024":[10,20,15,30],
                   "2025":[16,25,22,30],
                   "2026":[19,22,29,30]},index = ['A','B','C','D'])
df.plot(kind='bar',stacked = True)
plt.yticks(np.arange(0,100,10))
plt.grid(True)
plt.show()