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
"""
syntax : 
sns.scatterplot(data = dataset ,
             x = 'column name' ,
             y = 'column name' ,
             hue = 'column name',
             style = 'column name')
             
"""
sns.scatterplot(data = data,x = 'bill_length_mm',y = 'body_mass_g',
                hue = 'species',
                style = 'island',
                palette="ch:r=-.5,l=.75",
                size = 'species')
sns.set_style('darkgrid')
# The ways of styling themes are as follows:
# white
# dark
# whitegrid
# darkgrid
# ticks
sns.despine() #it will remove the upper and right part border of graph
"""
arguments:
1. hue : used to give color to the columns 
2. style : used to provide different symbol to each column 
3. size : used to give different sizes to the column
4. palette : used to change the color of column data
"""
"""
* set_context() allows us to override default parameters. This affects things like the size of the labels, Lines, and other elements of the plot, but
# poster
# Paper - Ideal for printing in academic papers.
# Notebook - Good for working inside Jupyter notebooks (default setting).
# talk - Good for presentation slides where readability matters.
"""
sns.set_context('paper')