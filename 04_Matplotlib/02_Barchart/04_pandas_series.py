import pandas as pd
import matplotlib.pyplot as plt
series = pd.Series([10,20,15,30],index = ['A','B','C','D'])
series.plot(kind = 'bar')
plt.title("Pandas Series To create Single Bar Chart")
plt.xlabel("Index Values at X-axis")
plt.ylabel("Data Values at Y-axis")
plt.show()