from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_sms(self,message:str):
        account_sid = os.environ.get("TWILO_ACCOUNT_SID") # Copied from my Dashboard remove config and write yours as a string
        auth_token = os.environ.get("TWILO_AUTH_TOKEN")  # Copied from my Dashboard  remove config and write yours as a string

        client = Client(account_sid, auth_token)

        message_t = client.messages \
            .create(
            body=message,
            from_=os.environ.get("TWILO_TO"),
            to=os.environ.get("TWILO_FROM")
        )

        print(message_t.sid)
        if message_t.status == "queued":
            print("Process Completed 100%")
