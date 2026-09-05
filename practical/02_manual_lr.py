import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("/Users/pratikvilasgadhe/Desktop/Programming/AI_ML/practical/Housing.csv")


x = df['area'].values
y = df['price'].values

#Calculate the means of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# 3. Calculate Slope (b1)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

b1 = numerator / denominator

# 4. Calculate Intercept (b0)
b0 = y_mean - (b1 * x_mean)

# h(x)
y_pred_manual = b0 + (b1 * x)


rmse_manual = np.sqrt(np.mean((y - y_pred_manual) ** 2))

# Manual R-squared (R2) Score
ss_residual = np.sum((y - y_pred_manual) ** 2)  # Sum of squared errors
ss_total = np.sum((y - y_mean) ** 2)           # Total sum of squares
r2_manual = 1 - (ss_residual / ss_total)

# Print results
print(f"Slope (b1): {b1}")
print(f"Intercept (b0): {b0}")
print(f"RMSE: {rmse_manual}")
print(f"R2 Score: {r2_manual}")
