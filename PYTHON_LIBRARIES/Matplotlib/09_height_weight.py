import pandas as pd
import matplotlib.pyplot as plt
height = [111.8,120.5,123.4,129.5,134.4,142.5,150.5,152.0,163.7]
weight = [20.5,21.5,24.6,25.6,27.4,30.2,35.2,38.8,45.4]
df = pd.DataFrame({"height":height,"weight":weight})
plt.xlabel("weight in kg")
plt.ylabel("height in cm")
plt.title("Height Vs Weight")
plt.plot(df.weight,df.height,marker = "*",markersize = 10,color = "black",linewidth = 2 , linestyle = ":",label = "weight")
plt.legend()
plt.grid(True)
# plt.yticks(df.height)
# plt.xticks(df.weight)
plt.show()