import requests

url = "https://api.github.com/users/github"

response = requests.get(url)

data = response.json()

print("Username:", data["login"])
print("Followers:", data["followers"])