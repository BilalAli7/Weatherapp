import requests
import json
import os


city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=5e3efb5d7625432c93983016232907&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
x = wdic["current"]["temp_f"]
os.system(f"say 'the current weather of {city} in celsius is {w} and in fahrenheit is {x}'")
print(f'The current weather of {city} in celsius is {w} and in fahrenheit is {x}')