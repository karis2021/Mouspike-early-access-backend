import os
import smtplib
from email.message import EmailMessage
def send_thank_you_email(to_email: str):
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    FROM_EMAIL = os.getenv("FROM_EMAAIL", SMTP_USER)
    if not SMTP_HOST or not SMTP_USER or not SMTP_PASS:
        print("Email not sent: SMTP config missing")
        return
    msg = EmailMessage()
    msg["Subject"] = "Mouspike Early Access - Request received"
    msg["From"] = FROM_EMAIL
    msg["to"] = to_email
    msg.set_content(
        "Thanks for requesting early access.\n"
        "Access is limit. No second chances.\n\n"
        "- Mouspike (London, UK)"
    ) 
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)