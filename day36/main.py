import requests as rq
import os
from twilio.rest import Client
import time


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

FROM_NUM = os.environ.get("FROM_NUM")
TO_NUM = os.environ.get("TO_NUM")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERC_CHANGE = -4.0

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("API_TOKEN")
}

print(f"{parameters}")

response = rq.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

time_series_data = data["Time Series (Daily)"]

count = 0
for k in time_series_data:
    if count == 2:
        break
    if count == 0:
        yest_close = time_series_data[k]['4. close']
    else:
        prev_close = time_series_data[k]['4. close']
    count += 1

percentage_change = round( (float(yest_close) - float(prev_close))/ float(yest_close) * 100, 3)

if percentage_change > abs(PERC_CHANGE) or percentage_change < PERC_CHANGE:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": os.environ.get("NEWS_API_TOKEN"),
        "pageSize": 2,
        "page": 1
    }

    response = rq.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    news_data = response.json()["articles"]

    for x in news_data:
        if percentage_change > 0.0:
            sms_text = f"{STOCK} 🔺{percentage_change}%\nHeadline: {x['title']}\nBrief: {x['description']}"
        else:
            sms_text = f"{STOCK} 🔻{percentage_change}%\nHeadline: {x['title']}\nBrief: {x['description']}"
        print(f"{sms_text}")

        message = client.messages.create(
                                            body=f"{sms_text}",
                                            from_=FROM_NUM,
                                            to=TO_NUM
        )

        print(f"{message.status}")
        time.sleep(5)


