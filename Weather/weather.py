import requests
import json
import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



api_key = "b34c6d76f637b53a643f76ee3ee87444"

country = input("Please write a country or city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}"


response = requests.get(url)
# Exchange rates (1 unit of each currency to DKK)
if response.status_code == 200:
    data = response.json()
    print(data)


# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Icons Example")

# Create a ttk.Style object and load the CSS
style = ttk.Style()
style.configure("Weather.TLabel", font=("Weather Icons", 24))

# Create a label with a weather icon
weather_label = ttk.Label(root, text="\uf00d", style="Weather.TLabel")
weather_label.pack()

root.mainloop()
