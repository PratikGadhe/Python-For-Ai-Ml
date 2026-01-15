import requests
# latitude = 48.85
# longitude = 2.35
# url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# response = requests.get(url)
# data = response.json()
# data.keys()
# print(data["current"]["temperature_2m"])
def temp(latitude,longitude):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response=requests.get(url)
    data=response.json()
    temp=data["current"]["temperature_2m"]
    return temp
lat=float(input("Enter latitude : "))
lon=float(input("Enter longitude : "))
final_temp=temp(lat,lon)
print(f"Temperature of your latitude({lat}) & longitude({lon}) is {final_temp}")