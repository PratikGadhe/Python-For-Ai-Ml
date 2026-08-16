import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'name':['anuj','shruti','rinku','vinay','akash','neha'],
                     'height':[60,62,68,66,72,70]})
data.plot(kind='hist',color=['black'])
plt.xlabel("No. of Bins/groups ")
plt.ylabel("No. of Frequency ")
plt.title("Foundation of histogram ")
plt.xticks(data.height)
plt.yticks()
plt.grid(True)
plt.show()
