import requests
import json
import datetime



api_key = "b34c6d76f637b53a643f76ee3ee87444"

country = input("Please write a country or city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}"


response = requests.get(url)
# Exchange rates (1 unit of each currency to DKK)
if response.status_code == 200:
    data = response.json()
    print(data)
