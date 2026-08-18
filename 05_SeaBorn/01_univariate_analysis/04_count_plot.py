import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

sns.get_dataset_names()
data = sns.load_dataset('penguins')
data.info()
data.describe()
data.describe(include = [object])
data.isnull().sum()

sns.countplot(data , x = 'species',hue = 'island')