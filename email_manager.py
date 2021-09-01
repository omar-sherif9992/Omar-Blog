import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class EmailManager:

    def send_email(self,title:str ,message: str, to_addrs: str, first_name: str, last_name: str):
        my_email =os.environ.get('MY_EMAIL') # the part after the @ is the identity of my email provider
        my_password = os.environ.get('MY_PASSWORD')
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            # location of our email provider
            # connection.starttls()  # to secure the email
            connection.login(user=my_email, password=my_password)  # login to your email
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addrs,
                                msg=f"Subject: {title}\n\nDear {first_name} {last_name},\n\n\n {message}.")  # sending the email