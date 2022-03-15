import datetime as dt
import random
import smtplib as smtp

now = dt.datetime.now()

if now.weekday() == 1:
    print("Today is Tuesday")


username = input("Enter Google Email:")
passWd = input("Enter password:")

# Get all quotes
quotes = []
with open(file="data/quotes.txt", mode="r") as fh:
    quotes = fh.readlines()

with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    # After starttls
    connection.login(user=username, password=passWd)
    connection.sendmail(
        from_addr=username,
        to_addrs="manoj7shekhawat@gmail.com",
        msg=f"Subject: Quote of the day\n\n{random.choice(quotes)}"
    )
