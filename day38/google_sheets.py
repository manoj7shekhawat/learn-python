import requests as req
import json
import datetime as dt
import os

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

query = input("How much did you exercise today? ")
#query = "i ran 3 miles and walked 2 miles"

body = {
    "query": query
}

response = req.post(url=URL, json=body, headers=headers)
response.raise_for_status()
ex_data = response.json()["exercises"]
print(f"{json.dumps(ex_data, indent=4, sort_keys=True)}")

# Sheety URL

SHEETY_URL = os.environ.get("SHEETY_URL")

headers = {
    "Authorization": os.environ.get("AUTHZ_TOKEN"),
    "Content-Type": "application/json"
}

today = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

for row in ex_data:
    body = {
        "workout": {
            "date": str(today),
            "time": str(time),
            "exercise": row['name'].title(),
            "duration": row['duration_min'],
            "calories": row['nf_calories']
        }
    }

    print(f"{body}")

    response = req.post(url=SHEETY_URL, json=body, headers=headers)
    response.raise_for_status()
    print(f"{response.text}")