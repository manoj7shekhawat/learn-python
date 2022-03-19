import os
import json
import requests as req
import datetime as dt

class FlightSearch:

    def __init__(self, city):
        super().__init__()

        self.url = "https://tequila-api.kiwi.com/locations/query"

        self.city = city

        self.headers = {
            "accept": "application/json",
            "apikey": os.environ.get("T_API_KEY")
        }

    def get_iat_code(self) -> str:

        parameters = {
            "term": self.city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "10",
            "active_only": "true"

        }

        response = req.get(url=self.url, params=parameters, headers=self.headers)
        response.raise_for_status()
        iat_code = response.json()["locations"][0]["id"]
        print(f"{iat_code}")
        return iat_code


    def get_lowest_return_price(self, to_city):
        # curl -X GET "https://tequila-api.kiwi.com/v2/search
        # ?&fly_to=CDG&date_from=18%2F03%2F2022&date_to=17%2F09%2F2022&nights_in_dst_from=7&nights_in_dst_to=28
        # &max_fly_duration=20&flight_type=round&one_for_city=0&one_per_date=0&adults=1&children=0&only_working_days=false&only_weekends=false
        # &partner_market=us&curr=GBP&max_stopovers=0&max_sector_stopovers=0&vehicle_type=aircraft&sort=price&asc=1&limit=1"
        # -H  "accept: application/json" -H  "apikey: eDfyOIegfdgdhjkhjllUXgD0SmeqMvK4fVik"
        parameters = {
            "fly_from": "LON",
            "fly_to": to_city,
            "date_from": (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (dt.datetime.now() + dt.timedelta(days=30*6)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "max_fly_duration": "20",
            "flight_type": "round",
            "one_for_city": "0",
            "one_per_date": "0",
            "adults": "1",
            "children": "0",
            "only_working_days": "false",
            "only_weekends": "false",
            "partner_market": "us",
            "curr": "GBP",
            "max_stopovers": "2",
            "max_sector_stopovers": "2",
            "vehicle_type": "aircraft",
            "sort": "price",
            "asc": "1",
            "limit": "1"
        }

        #print(f"{json.dumps(parameters, indent=4)}")
        response = req.get(url="https://tequila-api.kiwi.com/v2/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        #print(f"{data}")
        return response.json()["data"][0]
