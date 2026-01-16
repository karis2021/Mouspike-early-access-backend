import os
import requests

def send_thank_you_email(to_email: str) -> None:
    api_key = os.getenv("RESEND_API_KEY")
    from_email = os.getenv("FROM_EMAIL", "onboarding@resend.dev")
    reply_to = os.getenv("REPLY_TO", "iriscita_9@hotmail.com")
    if not api_key:
        print("Missing RESEND_API_KEY")
        return
    payload = {
        "from": from_email,
        "to": [to_email],
        "subject": "Mouspike Early Access - Request received",
        "text": (
            "Welcome to Mouspike.\n\n"
            "You're now inside Early Access.\n\n"
            "No re-entry.\n"
            "No repeats.\n"
            "You'll hear from us first.\n\n"
            "— MOUSPIKE (London, UK)\n"
        ),
        "reply_to": reply_to,
    }
    r = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=payload,
        timeout=20,
    )
    if r.status_code >= 400:
        raise Exception(f"Resend error {r.status_code}: {r.text}")

    print("Email sent via Resend:", r.json())
