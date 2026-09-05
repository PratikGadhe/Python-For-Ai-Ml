import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/pratikvilasgadhe/Desktop/Programming/AI_ML/titanic/train.csv')
df.columns
print("data visualization")
plt.figure()
sns.countplot(data = df , x = df['Survived'])
plt.title("distribution of survival")
plt.xlabel("survived")
plt.ylabel("passenger count")
plt.savefig("titanic.png")
plt.show()
plt.close()

# 3.
plt.figure(figsize = (8,6))