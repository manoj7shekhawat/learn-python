import requests as rq


MY_LAT = 51.107883
MY_LON = 17.038538

API_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "a8cf7189a8d61d70236727b3bd8f9ede"

# https://api.openweathermap.org/data/2.5/onecall?lat=51.107883&lon=17.038538&exclude=minutely&units=metric&appid=a8cf7189a8d61d70236727b3bd8f9ede

parameters = {
    "appid": API_KEY,
    "units": "metric",
    "exclude": "minutely,daily,current",
    "lat": MY_LAT,
    "lon": MY_LON
}

response = rq.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()

isGoingToRain = False
for x in range(0, 12):
    weather = data['hourly'][x]['weather']

    print(f"{weather}")
    for y in weather:
        if int(y['id']) < 700:
            isGoingToRain = True


if isGoingToRain:
    print(f"It's going to rain. Don't forgot the Umbrella :-)")