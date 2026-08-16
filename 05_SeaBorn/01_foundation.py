import seaborn as sns
import pandas as pd

# to show the available datasets in seaborn
print(sns.get_dataset_names())

# to load the dataset from available dataset in seaborn 
dataset = sns.load_dataset('penguins')
print(dataset.head())
print(dataset.columns)

# to count the number of species in 'species column'
print(dataset['species'].value_counts())
print(dataset['island'].value_counts())

# descriptive analysis :
#1. no. of columns , no of rows , no of non null value
print(dataset.info()) 

#2. it calculates count,mean ,std , max ,25% ,50%,75% of each columns
print(dataset.describe()) 
print(dataset.describe().T)

# 3.  it will show the description about categorical data/unique data
print(dataset.describe(include = [object]))

# 4. to find the null values of each column/feature
print(dataset.isnull().sum())
print(dataset.duplicated().sum()) #Returns the number of duplicate rows in the dataset.
