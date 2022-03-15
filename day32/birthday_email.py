import random

import pandas as pd
import datetime as dt
import smtplib as smtp

now = dt.datetime.now()
mnt = now.month
day = now.day

birthday_person_name = None
birthday_person_email = None
# First read the birthdays.csv and get:
# name & email
data = pd.read_csv(filepath_or_buffer="birthdays.csv")

for index, row in data.iterrows():
    if row.month == mnt and row.day == day:
        birthday_person_email = row.email
        birthday_person_name = row["name"]

if birthday_person_name is not None and birthday_person_email is not None:
    print(f"Name:: {birthday_person_name} Email:: {birthday_person_email}")

    # Read random files
    filename = "letter_" + str(random.randint(1, 3)) + ".txt"

    with open(file=f"letter_templates/{filename}", mode="r") as fh:
        lines = fh.readlines()

    lines_to_send = [x.replace("[NAME]", birthday_person_name) for x in lines]

    print(f"{lines_to_send}")

    user_name = input("Enter email: ")
    user_pass = input("Password: ")

    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_name, password=user_pass)
        connection.sendmail(from_addr=user_name, to_addrs=birthday_person_email,
                            msg=f"Subject: Happy Birth Day\n\n{''.join(lines_to_send)}")

    print("Email Sent :-)")
else:
    print("No birthday today :-)")
