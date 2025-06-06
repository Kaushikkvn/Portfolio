import requests

def send_email(message, user_email):
    form_url = "https://formsubmit.co/el/juhuge"

    data = {
        "name": "Streamlit Contact Form",
        "email": user_email,
        "message": message
    }

    response = requests.post(form_url, data=data)

    if response.status_code == 200:
        print("✅ Message sent via Formsubmit!")
    else:
        print("❌ Failed to send message. Code:", response.status_code)
