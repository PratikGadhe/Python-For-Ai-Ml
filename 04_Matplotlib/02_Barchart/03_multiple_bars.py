import matplotlib.pyplot as plt
year = [2022,2023,2024,2025,2026]
mi = [6,7,8,2,4]
rcb = [5,8,2,4,2]

plt.bar(year,mi,color = 'blue' , label = 'Mumbai')
plt.bar(year,rcb,color = 'red' , label = 'Rcb')

plt.xlabel("Last 5 years")
plt.ylabel("Stats")
plt.title("Mumbai Vs Rcb")
plt.xticks(year)
plt.show()