import requests
import json

hakusana = input("Enter municipality name: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid=449056980a6ef6abb76bf3e781782809&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        sää = vastaus.json()
        weather = sää["weather"][0]["main"]
        description = sää["weather"][0]["description"]
        temperature = sää["main"]["temp"]
        print(f"Weather: {weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature} Celsius")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")