from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from email_service import send_thank_you_email
from email_service import send_welcome_email
from database import init_db, insert_email, list_signups

app = FastAPI(title="Mouspike Early Access API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://karis2021.github.io",
    "http://127.0.0.1:5500",
    "http://localhost:5500"],
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
    email = payload.email
    result = insert_email(payload.email)
    if result["inserted"]:
        send_thank_you_email(payload.email)
        send_welcome_email(email)
        return{
        "status": "ok",
        "message": "Email Registered Successfully",
        "email": payload.email
    }
    return{
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