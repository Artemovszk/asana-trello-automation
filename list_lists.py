import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
board_id = os.getenv("TRELLO_BOARD_ID")

url = f"https://api.trello.com/1/boards/{board_id}/lists"
params = {"key": key, "token": token}

r = requests.get(url, params=params)
for l in r.json():
    print(l["name"], "->", l["id"])
