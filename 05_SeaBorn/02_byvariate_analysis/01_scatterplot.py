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

# scatter plot visualization (numeric to numeric)
# syntax : sns.scatterplot(data = dataset , x = 'column name' , y = 'column name')
sns.scatterplot(data = data,x = 'bill_length_mm',y = 'body_mass_g',color = 'red')
sns.set_style('ticks')
# The ways of styling themes are as follows:
# white
# dark
# whitegrid
# darkgrid
# ticks