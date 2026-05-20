import numpy as np
import matplotlib.pyplot as plt
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000 ,240000, 280000],
    [5, 160000, 185000, 205000, 230000]
])

print("--- ZOMATO SALES ANALYSIS ---")

print("Sales Data Shape : ",sales_data.shape)

print("1. First Three data : ",sales_data[:3])
print("2. First Three data : ",sales_data[:3,1:])

# total sales per year 
print(np.sum(sales_data,axis = 0))
print(np.sum(sales_data[:,1:],axis = 0))

# minimum by column and row 
print("column : ",np.min(sales_data[:,1:],axis = 0))
print("row : ",np.min(sales_data[:,1:],axis = 1))

# maximum by column and row 
print("column : ",np.max(sales_data[:,1:],axis = 0))
print("row : ",np.max(sales_data[:,1:],axis = 1))

# average by column and row 
print("column : ",np.mean(sales_data[:,1:],axis = 0))
print("row : ",np.mean(sales_data[:,1:],axis = 1))

# cumulate 
print("cumulate sale : ",np.cumsum(sales_data[:,1:],axis = 1))

# showing data on graph (matplotlib)
cumsum = np.cumsum(sales_data[:,1:],axis = 1)
plt.figure(figsize=(10,6))
plt.plot(np.mean(cumsum,axis = 0))
plt.title("Average Cumulative Sales")
plt.xlabel("years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()