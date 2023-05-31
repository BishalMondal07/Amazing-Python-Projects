import requests
import json
city = input("Enter the name of the city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=769867e6d6b148e28be52858232603&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])