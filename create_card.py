import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
list_id = os.getenv("TRELLO_LIST_ID")

url = "https://api.trello.com/1/cards"
params = {
    "key": key,
    "token": token,
    "idList": list_id,
    "name": "Első automatikus kártya",
    "desc": "Ez a kártya a Python automatizációval jött létre."
}

r = requests.post(url, params=params)

if r.status_code == 200:
    print("Sikeresen létrehoztuk a kártyát!")
else:
    print("Hiba történt:", r.text)
