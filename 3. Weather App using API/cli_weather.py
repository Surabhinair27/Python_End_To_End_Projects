# 🌦️ Weather App (CLI Version)
# ------------------------------------
# API call se live weather data laayenge
# ------------------------------------

import requests                 # API request bhejne ke liye
from config import API_KEY      # apni key import


# 🔍 Weather fetch function
def get_weather(city):

    # 🌍 API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    # 📡 Request bhejo
    response = requests.get(url)

    # 📦 JSON me convert karo
    data = response.json()

    # ❌ Agar city galat
    if data["cod"] != 200:
        print("❌ City not found!")
        return

    # 📊 Data extract
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    # 🎯 Print result
    print("\n🌤️ Weather Report")
    print("---------------------")
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {desc}")


# ▶ Start program
city = input("Enter city name: ")
get_weather(city)
