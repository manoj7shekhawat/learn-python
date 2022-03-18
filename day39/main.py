import os
import json
import time

import requests as req
import datetime as dt

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

URL = "https://api.sheety.co/3e3b2cfc1cab392b047e49ea0660c5a3/flightDeals/prices"

headers = {
    "Authorization": os.environ.get("AUTH_TOKEN"),
    "Content-Type": "application/json"
}

response = req.get(url=URL, headers=headers)
response.raise_for_status()
sheet_data = response.json()["prices"]

print(f"{json.dumps(sheet_data, indent=4)}")

for city in sheet_data:
    fs = FlightSearch(city["city"])
    # city["iataCode"] = fs.get_iat_code()
    #
    # dm = DataManager(city["id"], city["city"], city["iataCode"], city["lowestPrice"])
    # dm.update_sheet_row()


    # Find the lowest price return ticket
    flight_data = fs.get_lowest_return_price(city["iataCode"])
    print(f"City: {city['city']} Price Found: £{flight_data['price']} Lowest Price: {city['lowestPrice']}")

    if int(flight_data['price']) < int(city["lowestPrice"]):
        # Send SMS
        print("Sending SMS")
        nm = NotificationManager(
            flight_data['price'],
            "London",
            city['city'],
            # TODO: Dummy dates
            from_date=str((dt.datetime.now() + dt.timedelta(days=1)).strftime("%d-%m-%Y")),
            to_date=str((dt.datetime.now() + dt.timedelta(days=1*60)).strftime("%d-%m-%Y"))
        )
        nm.send_sms()

    time.sleep(5)



#print(f"{json.dumps(sheet_data, indent=4)}")