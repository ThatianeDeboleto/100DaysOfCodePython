from twilio.rest import Client

TWILIO_SID = "0724ddf0effb330060f303ed3970ac6c"
TWILIO_AUTH_TOKEN = "ACc3a6f5cdae61c6a6e3dfb29e19dd11bd"
TWILIO_VIRTUAL_NUMBER = "+12079528447"
TWILIO_VERIFIED_NUMBER = "+5511964674101"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

