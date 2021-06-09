import requests 
from bs4 import BeautifulSoup


search = "weather in Seattle"

URL = f"https://www.google.com/search?q={search}"

req = requests.get(URL)
sav = BeautifulSoup(req.text, "html.parser")

update = sav.find("div", class_= "BNeawe").text
print(update)