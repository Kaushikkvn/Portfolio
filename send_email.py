import requests

def send_email(message, user_email):
    form_url = "https://formsubmit.co/el/juhuge"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "name": "Streamlit User",
        "email": user_email,
        "message": message,
        "_captcha": "false",
        "_template": "table"
    }

    response = requests.post(form_url, data=data, headers=headers)

    if response.status_code == 200:
        print("✅ Email sent via Formsubmit!")
    else:
        print("❌ Failed to send message. Status:", response.status_code)
        print("Response text:", response.text)
