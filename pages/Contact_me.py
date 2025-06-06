import streamlit as st
from send_email import send_email

st.header("📬 Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    # Required SMTP format: subject, from, blank line, body
    message = f"""\
Subject: New message from {user_email}
From: {user_email}

{raw_message}
"""

    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_email and raw_message:
            send_email(message)
            st.success("✅ Your message has been sent successfully!")
        else:
            st.warning("⚠️ Please fill out both fields before sending.")
