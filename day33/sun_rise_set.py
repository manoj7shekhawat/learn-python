import requests as rq
import datetime as dt

MY_LAT = 51.107883
MY_LONG = 17.038538

parameters = {
    #https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = rq.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"{sunrise} {sunset}")


today = dt.datetime.now()
print(f"{today}")