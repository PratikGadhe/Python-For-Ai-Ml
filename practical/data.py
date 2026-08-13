import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/pratikvilasgadhe/Desktop/Programming/AI:ML/titanic/train.csv')
print(df.head())

print(df.isnull().sum())
# copy database 
data_1 = df

# drop columns
data_1 = data_1.drop('Cabin',axis = 'columns')
print(data_1.columns)

# data imputation
# mean
data_1['Age'] = data_1['Age'].fillna(data_1['Age'].mean())
print(data_1.describe())

# mode
data_1['Embarked']=data_1['Embarked'].fillna(data_1['Embarked'].mode()[0])
print(data_1.describe())
print(data_1.isnull.sum())

print(df.columns)

# variant analysis : 
"""
1. uni variant 2. by variant 3. multivariant
"""
# for catagratical data : .countplot()
print(sns.countplot(x=df['Sex']))
print(sns.countplot(x=df['Embarked']))
print(sns.countplot(x=df['Pclass']))

# for numerical data : .boxplot()
print(sns.boxplot(x=df['Age']))