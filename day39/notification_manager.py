import os
from twilio.rest import Client

class NotificationManager:

    def __init__(self, price, frm, to, from_date, to_date):
        super().__init__()
        self.price = price
        self.frm = frm
        self.to = to
        self.from_date = from_date
        self.to_date = to_date


    def send_sms(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        FROM_NUM = os.environ.get("FROM_NUM")
        TO_NUM = os.environ.get("TO_NUM")

        sms_text = f"Low price alert! Only £{self.price} to fly from {self.frm} to {self.to} from date {self.from_date} to {self.to_date}"
        message = client.messages.create(
            body=f"{sms_text}",
            from_=FROM_NUM,
            to=TO_NUM
        )

        print(f"{message.status}")