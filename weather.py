import requests

city = input("Enter a city: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()

temperature = data["current_condition"][0]["temp_C"]

print("Temperature in", city, "is", temperature, "°C")