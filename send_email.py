import requests

def send_email(message, user_email):
    form_url = "https://formsubmit.co/el/juhuge"  # your verified Formsubmit link

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "name": "Streamlit Visitor",
        "email": user_email,
        "message": message,
        "_autoresponse": "Thanks for contacting me! I’ll get back to you soon.",
        "_captcha": "false",
        "_template": "table"
    }

    try:
        response = requests.post(form_url, data=data, headers=headers)
        if response.status_code == 200:
            print("✅ Email sent successfully!")
            return True
        else:
            print("❌ Error:", response.status_code, response.text)
            return False
    except Exception as e:
        print("❌ Exception while sending email:", e)
        return False
