import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("penguins")
data.columns
sns.lmplot(data,x='bill_length_mm',y='bill_depth_mm'
           , hue = 'species',
           col = 'sex')