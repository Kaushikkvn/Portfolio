import requests

def send_email(message, user_email):
    form_url = "https://formsubmit.co/el/juhuge"  # your verified endpoint

    data = {
        "name": "Streamlit Contact Form",
        "email": user_email,
        "message": message,
        "_autoresponse": "Thanks! I'll get back to you shortly.",
        "_captcha": "false",
        "_template": "table"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(form_url, data=data, headers=headers)

        if response.status_code == 200 or response.status_code == 302:
            print("✅ Form submitted successfully.")
            return True
        else:
            print("❌ Failed to submit form. Status:", response.status_code)
            print(response.text)
            return False

    except Exception as e:
        print("❌ Exception:", str(e))
        return False
