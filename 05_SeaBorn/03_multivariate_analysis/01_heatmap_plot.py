import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("penguins")
data.info()
data.describe()
data.columns
columns = ['bill_length_mm',	'bill_depth_mm',	'flipper_length_mm',	'body_mass_g']
sns.heatmap(data[columns].corr(),annot = True
            ,cmap = 'Blues'
            ,vmin = 0.2
            ,linewidth = 2
            ,linecolor = "black")