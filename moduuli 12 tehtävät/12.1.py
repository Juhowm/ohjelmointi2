import requests

vitsi = requests.get("https://api.chucknorris.io/jokes/random").json()
print(vitsi["value"])
