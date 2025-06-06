import requests

def send_email(message, user_email):
    form_url = "https://formsubmit.co/el/juhuge"  # your verified endpoint

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "name": "Streamlit Visitor",
        "email": user_email,
        "message": message,
        "_autoresponse": "Thanks for contacting me! I'll get back to you soon.",
        "_captcha": "false",
        "_template": "table",
        "_next": "https://portfolio-kaushikkommineni.streamlit.app/Contact_me"
    }

    response = requests.post(form_url, data=data, headers=headers)

    if response.status_code == 200:
        print("✅ Email sent via Formsubmit!")
    else:
        print("❌ Failed to send message. Status:", response.status_code)
        print("Response text:", response.text)
