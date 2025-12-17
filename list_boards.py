import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")

url = "https://api.trello.com/1/members/me/boards"
params = {"key": key, "token": token}

r = requests.get(url, params=params)
for b in r.json():
    print(b["name"], "->", b["id"])
