import requests
from datetime import datetime
import time
import smtplib as smtp

MY_LAT = 51.107883
MY_LONG = 17.038538

MY_EMAIL = "manojpolska@gmail.com"
MY_PASSWD = input("Enter Password: ")


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    print(f"{MY_LAT} {iss_latitude}\n{MY_LONG} {iss_longitude}\n{time_now.hour} {sunset} {sunrise}")
    if iss_latitude - 5.0 < MY_LAT < iss_latitude + 5.0 and iss_longitude - 5.0 < MY_LONG < iss_longitude + 5.0 \
            and sunset <= time_now.hour >= sunrise:
        print("Is is dark and ISS is close by, look up")
        with smtp.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWD)
            conn.sendmail(from_addr=MY_EMAIL, to_addrs="manoj7shekhawat@gmail.com",
                          msg=f"Subject:ISS Alert\n\nIs is dark and ISS is close by, look UP")
    else:
        print("ISS is far")

    time.sleep(60)