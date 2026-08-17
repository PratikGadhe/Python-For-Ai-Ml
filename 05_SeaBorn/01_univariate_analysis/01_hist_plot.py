import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset("penguins")
dataset.head()
dataset.describe()
dataset.info()

# histplot (distplot())
# categorical data
sns.histplot(data = dataset, x = 'species',hue = 'species')

# numerical values
sns.histplot(dataset , x = 'bill_length_mm',
             hue = "sex",
             binwidth = 2,
             bins = 20,
             shrink = 0.8,
             element="step",
            multiple="stack"
            )

# subplotting
sns.displot(dataset, x="flipper_length_mm", col="sex")