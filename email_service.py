import os
import requests
def send_admin_notification(new_user_email: str) -> None:
    api_key = os.getenv("RESEND_API_KEY")
    from_email = os.getenv("FROM_EMAIL", "onboarding@resend.dev")
    admin_email = os.getenv("TEST_RECEIVER_EMAIL")  # tu email permitido por Resend testing
    if not api_key:
        raise Exception("Missing RESEND_API_KEY")
    if not admin_email:
        raise Exception("Missing TEST_RECEIVER_EMAIL (your Resend testing email)")
    payload = {
        "from": from_email,
        "to": [admin_email],
        "subject": "New Early Access signup 🔥",
        "text": (
            "Someone just registered for Mouspike Early Access.\n\n"
            f"Email submitted: {new_user_email}\n\n"
            "— Mouspike Early Access Backend"
        ),
    }
    r = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=15,
    )
    if r.status_code >= 400:
        raise Exception(f"Resend error {r.status_code}: {r.text}")