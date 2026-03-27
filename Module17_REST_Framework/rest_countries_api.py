import requests

url = "https://restcountries.com/v3.1/name/india"

response = requests.get(url)

data = response.json()

print("Country:", data[0]["name"]["common"])
print("Capital:", data[0]["capital"][0])