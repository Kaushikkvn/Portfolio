import os
import smtplib
import ssl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(message):
    host="smtp.gmail.com"
    port=465
    username="venkatakommineni30@gmail.com"
    password=os.getenv("PASSWORD")
    receiver="venkatakommineni30@gmail.com"
    print(password)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)