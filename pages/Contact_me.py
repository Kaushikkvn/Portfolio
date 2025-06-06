import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me", page_icon="📬")
st.header("📬 Contact Me")

with st.form("contact_form"):
    user_email = st.text_input("Your email address", placeholder="you@example.com")
    message_body = st.text_area("Your message", height=150)

    if st.form_submit_button("Send"):
        if user_email and message_body:
            message = f"From: {user_email}\n\n{message_body}"
            sent = send_email(message, user_email)
            if sent:
                st.success("✅ Message sent successfully!")
            else:
                st.error("❌ Failed to send message. Try again later.")
        else:
            st.warning("⚠️ Please fill in all fields.")
