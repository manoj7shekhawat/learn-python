import os
import requests as req



class DataManager:

    USER_SHEET_URL = "https://api.sheety.co/3e3b2cfc1cab392b047e49ea0660c5a3/flightDeals/users"

    HEADERS = {
        "Authorization": os.environ.get("AUTH_TOKEN"),
        "Content-Type": "application/json"
    }

    def __init__(self, id, city, iata_code, lowest_price, first_name, last_name, email_id):
        self.url = "https://api.sheety.co/3e3b2cfc1cab392b047e49ea0660c5a3/flightDeals/prices/"
        self.id = id
        self.city = city
        self.iataCode = iata_code
        self.lowestPrice = lowest_price
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id


    def add_user(self):
        body = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email_id
            }
        }

        response = req.post(url=DataManager.USER_SHEET_URL, json=body, headers=DataManager.HEADERS)
        response.raise_for_status()
        print(f"{response.text}")

    def update_sheet_row(self):

        body = {
            "price": {
                            "city": self.city,
                            "iataCode": self.iataCode,
                            "lowestPrice": str(self.lowestPrice)
            }
        }

        print(f"{body}")
        response = req.put(url=self.url + str(self.id), json=body, headers=DataManager.HEADERS)
        response.raise_for_status()
        print(f"{response.text}")