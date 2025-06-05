import smtplib
import ssl
import streamlit as st

def send_email(message):
    host = "smtp-relay.brevo.com"
    port = 587
    username = st.secrets["BREVO_USERNAME"]
    password = st.secrets["BREVO_PASSWORD"]
    receiver = "venkatakommineni30@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("✅ Email sent!")

