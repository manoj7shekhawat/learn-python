import os
import requests as req



class DataManager:

    def __init__(self, id, city, iataCode, lowestPrice):
        self.url = "https://api.sheety.co/3e3b2cfc1cab392b047e49ea0660c5a3/flightDeals/prices/"

        self.id = id
        self.city = city
        self.iataCode = iataCode
        self.lowestPrice = lowestPrice



    def update_sheet_row(self):
        headers = {
            "Authorization": os.environ.get("AUTH_TOKEN"),
            "Content-Type": "application/json"
        }

        body = {
            "price": {
                            "city": self.city,
                            "iataCode": self.iataCode,
                            "lowestPrice": str(self.lowestPrice)
            }
        }

        print(f"{body}")
        response = req.put(url=self.url + str(self.id), json=body, headers=headers)
        response.raise_for_status()
        print(f"{response.text}")