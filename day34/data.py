import requests as rq

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = rq.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]