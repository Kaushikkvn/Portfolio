import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp-relay.brevo.com"
    port = 587
    username = os.getenv("BREVO_USERNAME")
    password = os.getenv("BREVO_PASSWORD")
    receiver = "venkatakommineni30@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("✅ Email sent!")
