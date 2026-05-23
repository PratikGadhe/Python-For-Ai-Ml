import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({"2024":[10,20,15,30],
                   "2025":[16,25,22,30],
                   "2026":[19,22,29,32]},index = ['A','B','C','D'])
df.plot(kind='bar',stacked = True)
plt.show()