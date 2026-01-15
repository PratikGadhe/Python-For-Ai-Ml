import requests
from datetime import datetime , timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
today = datetime.now()
week_ago = today - timedelta(days=7)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today. strftime("%Y-%m-%d")
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data=response.json()
data.keys()

daily_data = data["daily"]

df = pd.DataFrame({"Date":daily_data["time"],"Max_Temp":daily_data["temperature_2m_max"]
                   ,"Min_Temp":daily_data["temperature_2m_min"]})
df['Date']=pd.to_datetime(df["Date"])
print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Max_Temp'], marker='o', label='Max Temp')
plt.plot(df['Date'], df['Min_Temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()



# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")