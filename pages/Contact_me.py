import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me", page_icon="📬")
st.title("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")

    if st.form_submit_button("Send"):
        if name and email and message:
            if send_email(name, email, message):
                st.success("✅ Message sent successfully!")
            else:
                st.error("❌ Failed to send. Please try again later.")
        else:
            st.warning("⚠️ Please fill out all fields.")
