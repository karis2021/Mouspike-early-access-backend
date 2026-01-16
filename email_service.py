import os
import smtplib
from email.message import EmailMessage
def send_thank_you_email(to_email: str) -> None:
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.office365.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    if not SMTP_USER or not SMTP_PASS:
        print("SMTP missing env vars (SMTP_USER / SMTP_PASS).")
        return

    msg = EmailMessage()
    msg["Subject"] = "Mouspike Early Access - Request received"
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg.set_content(
        "Welcome to Mouspike.\n\n"
        "You're now inside Early Access.\n\n"
        "No re-entry.\n"
        "No repeats.\n"
        "You'll hear from us first.\n\n"
        "— MOUSPIKE (London, UK)\n"
        )
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print(f"EMail sent to {to_email}")
    except Exception as e:
        print("Email send failed:", repr(e))