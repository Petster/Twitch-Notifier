import smtplib
import sys
import config

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com"
}

EMAIL = config.EMAIL
PASSWORD = config.EMAIL_PASSWORD

def send_message(phone_number, carrier, message):
    recipient = str(phone_number) + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], recipient, message)


if __name__ == "__main__":
    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[3]

    send_message(phone_number, carrier, message)