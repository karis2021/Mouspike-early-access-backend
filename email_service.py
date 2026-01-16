import os
import smtplib
from email.message import EmailMessage
def send_thank_you_email(to_email: str):
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

def send_welcome_email(to_email: str):
    msg = EmailMessage()
    msg["Subject"] = "Mouspike Early Access - Request received"
    msg["From"] = SMTP_USER
    msg["to"] = to_email
    msg.set_content("""
        Welcome to Mouspike.

        You're now inside Early Access.

        No re-entry.
        No repeats.
        You'll hear from us first.

        — MOUSPIKE (London, UK)
        """)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)