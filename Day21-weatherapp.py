import requests 
from datetime import datetime
import time
api_key = "enter your api key" #replace this with your own api key
city=input("Enter city name: ")
print(city)
weather_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(weather_url)
if response.json()["cod"]=="404":
    print("city not found")
else:
    weather=response.json()["weather"][0]["description"]
    temp =response.json()["main"]["temp"]
    humidity =response.json()["main"]["humidity"]
    sunrise = response.json()["sys"]["sunrise"]
    sunset = response.json()["sys"]["sunset"]
    print(f"Temperature in {city}: {temp}°C")
    print(f"Description: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Sunrise: {datetime.fromtimestamp(sunrise)}")
    print(f"Sunset: {datetime.fromtimestamp(sunset)}")
