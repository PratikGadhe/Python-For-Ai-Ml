import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OneHotEncoder , StandardScaler
df = pd.read_csv('/Users/pratikvilasgadhe/Desktop/Programming/AI_ML/titanic/train.csv')
print(df.head())

# featuring engineering
print("Feature Engineering and preprocessing")

# create family size and isalone features 
df['family_size'] = df['SibSp'] + df['Parch'] + 1
df['is_alone'] = (df['family_size'] == 1).astype(int)

print("Engineered new features : 'family_size' and 'is_alone' ")
df.columns
df.shape


# drop columns with excessive missing data or redundant representation
column_drop = ['cabin']
df_clean = df.drop(columns = [ col for col in column_drop if col in df.columns])
df_clean.shape
# separate features (x) and target (y)
x = df_clean.drop(columns = ['Survived'])
y = df_clean['Survived']
print(x.shape)
print(y.shape)

# identify numerical and categorical features
n_cols = x.select_dtypes(include=[np.number]).columns.tolist()
c_cols = y.select_dtypes(include=['object','category','bool'].columns.tolist())

print(f"\n Numerical Columns ({len(n_cols)}) : {n_cols}")
print(f"\n Categorical Columns ({len(c_cols)}) : {c_cols}")

n_transormer = Pipeline(
    steps = [
        ("imputer",SimpleImputer(strategy = 'median')),
        ('scaler',StandardScaler()),
    ]
)

c_transformer = Pipeline(
    steps = [
        ('imputer',SimpleImputer(strategy = 'most_frequent')),
        ('onehot',OneHotEncoder()),
    ]
)