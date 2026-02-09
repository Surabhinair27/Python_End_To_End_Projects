# 🌦️ Weather App GUI using Tkinter
# -----------------------------------
# City enter karo → button click → weather show
# -----------------------------------

import tkinter as tk
import requests
from config import API_KEY


# 🔍 Weather function
def get_weather():

    city = entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        result_label.config(text="❌ City not found!")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    result = (
        f"🌡 Temp: {temp}°C\n"
        f"💧 Humidity: {humidity}%\n"
        f"🌥 Condition: {desc}"
    )

    result_label.config(text=result)


# 🪟 Window
root = tk.Tk()
root.title("Weather App 🌦️")
root.geometry("300x250")


title = tk.Label(root, text="Enter City Name", font=("Arial", 12))
title.pack(pady=10)


entry = tk.Entry(root)
entry.pack(pady=5)


btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)


root.mainloop()
