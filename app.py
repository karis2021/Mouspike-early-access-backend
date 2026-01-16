import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from email_service import send_admin_notification
from database import init_db, insert_email, list_signups

app = FastAPI(title="Mouspike Early Access API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return{"status":"ok"}

class SignupRequest(BaseModel):
    email: str

@app.post("/signup")
def signup(payload: SignupRequest):
    email = payload.email.strip().lower()
    print("EMAIL RECEIVED:", email)
    result = insert_email(email)

    if result["inserted"]:
        demo_receiver = os.getenv("TEST_RECEIVER_EMAIL", email)
    try:
        send_admin_notification(email)
    except Exception as e:
        print("Admin email failed:", repr(e))
        return {
            "status": "ok",
            "message": "Email Registered Successfully",
            "email": email,
        }
    return {
        "status": "exists",
        "message": "Email already registered",
        "email": email
    }
@app.get("/signups")
def get_signups(limit: int = 100):
    items = list_signups(limit)
    return {"count": len(items), "items": items}