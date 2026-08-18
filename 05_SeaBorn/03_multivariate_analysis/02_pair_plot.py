import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("penguins")

sns.pairplot(data,hue = 'sex',diag_kind = 'kde')
sns.pairplot(data,hue = 'sex',kind = 'kde')