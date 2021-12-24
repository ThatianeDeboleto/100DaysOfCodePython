import smtplib
import datetime as dt
import random

import quote as quote
#enviar msg para email
MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL
        )
        print(f"Subject:Quarta Motivacional\n\n{quote}")

