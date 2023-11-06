import requests
import json

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={372576880cc1ce2ce575eea01430304e}
#sijaintimuunnos

kp = input("Anna paikkakunnan nimi: ")
sää = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={kp}&appid=372576880cc1ce2ce575eea01430304e&lang=fi&units=metric").json()
if sää["cod"] == "404":
    print("404: kaupunkia ei löydy")
else:
    lp = sää["main"]["temp"]
    w = sää["weather"][0]["description"]
    print(f"Paikkakunnan lämpotila on {lp} celsiusastetta")
    print(f"ja säätila on {w}.")
