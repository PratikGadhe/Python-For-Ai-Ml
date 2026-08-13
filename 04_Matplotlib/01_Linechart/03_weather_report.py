import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('weather_report.csv')
df.plot(kind = "line",color = ['red','blue','green','black'],marker = "*")
plt.grid(True)
plt.title("Weather Report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()