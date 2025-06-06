import requests

def send_email(name, email, message):
    service_id = "service_dqs7juv"
    template_id = "template_xu04l3e"
    public_key = "b-YacL-7og63Yqzic"

    payload = {
        "service_id": service_id,
        "template_id": template_id,
        "user_id": public_key,
        "template_params": {
            "from_name": name,
            "from_email": email,
            "message": message
        }
    }

    try:
        response = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=payload)
        if response.status_code == 200:
            print("✅ Email sent successfully!")
            return True
        else:
            print("❌ Failed. Status:", response.status_code)
            print("Response:", response.text)
            return False
    except Exception as e:
        print("❌ Exception:", e)
        return False

