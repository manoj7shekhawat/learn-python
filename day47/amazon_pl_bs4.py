import os
from bs4 import BeautifulSoup
import requests as req
import smtplib as smtp


HIT_PRICE = 400.00
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASS = os.environ.get("USER_PASS")

MY_EMAIL = "manoj7shekhawat@gmail.com"

url = "https://www.amazon.pl/gp/product/B07W5JK1JN/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}
response = req.get(url=url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find("span", class_="a-offscreen").getText()
print(f"{price}")
# clean price to float
price = float(price.split(",")[0])
print(f"{price}")


if price < HIT_PRICE:
    # send email
    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASS)
        connection.sendmail(from_addr=USER_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject: Amazon Lottery\n\nLogitech Mx Keys Advanced Wireless is below 400 PLN, grap it now")
else:
    print("Not in our range :-(")