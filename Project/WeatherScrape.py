import requests 
from bs4 import BeautifulSoup


search = "weather in india"

URL = f"https://www.google.com/search?q={search}"

req = requests.get(URL)
sav = BeautifulSoup(req.text, "html.parser")

update = sav.find("div", class_= "BNeawe").text
print(update)

newString = update.split("°", 1)

finString = newString[0]

print(finString)

if (int(finString) > 70):
    print("youre in hell")
else:
    print("stay inside and cry")