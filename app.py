from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from email_service import send_thank_you_email
from database import init_db, insert_email, list_signups

app = FastAPI(title="Mouspike Early Access API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://karis2021.github.io"],
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
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
    result = insert_email(email)

    if result["inserted"]:
        try:
            send_thank_you_email(email)
        except Exception as e:
            print("Welcome email failed:", repr(e))
        return {
            "status": "ok",
            "message": "Email Registered Successfully",
            "email": email
        }
    return {
        "status": "Exists",
        "message": "Email already registered",
        "email": email
    }
@app.get("/signups")
def get_signups(limit: int = 100):
    return {
        "count": len(list_signups(limit)),
        "items": list_signups(limit)
    }