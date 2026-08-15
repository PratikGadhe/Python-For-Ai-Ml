import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/04_Matplotlib/01_Linechart/weather_report.csv')
print(df)
df.plot(kind='bar',stacked = True)
plt.xlabel("index")
plt.ylabel("data")
plt.title("Csv Data visualization using pandas")
plt.yticks(np.arange(0,210,10))
plt.grid(True)
plt.show()