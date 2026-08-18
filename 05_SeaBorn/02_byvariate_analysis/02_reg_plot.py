import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# scatter plot is used for the relationship between two variables or more than two variables
# load dataset and analysis of data
data = sns.load_dataset('penguins')
print(data.head())
print(data.info())
print(data.describe().T)
print(data.describe(include = [object]))
print(data.isnull().sum())

sns.regplot(data , x = 'bill_length_mm' , y = 'bill_depth_mm',order=2)