import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me", page_icon="📬")
st.header("📬 Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address", placeholder="you@example.com")
    raw_message = st.text_area("Your message", height=150, placeholder="What would you like to say?")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_email and raw_message:
            send_email(raw_message, user_email)
            st.success("✅ Your message has been sent!")
        else:
            st.warning("⚠️ Please fill out both fields.")
