import requests

city = "London"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=demo"

response = requests.get(url)

print(response.text)