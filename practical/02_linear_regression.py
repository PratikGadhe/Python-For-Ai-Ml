import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

df = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI_ML/practical/Housing.csv")
# linear regression using scikit learn (direct method)
# area vs price
y_price = df['price'].values
x_area = df[['area']] #2d array for scikit learn

lr_simple = LinearRegression()
lr_simple.fit(x_area , y_price)
y_pred_simple = lr_simple.predict(x_area)

# Metrics
rmse_simple = np.sqrt(mean_squared_error(y_price, y_pred_simple))
print(rmse_simple)
r2_simple = r2_score(y_price, y_pred_simple)
print(r2_simple)