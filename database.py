import sqlite3
from datetime import datetime
from typing import List, Dict, Any 
DB_PATH = "signup.db"
def get_connection():
    return sqlite3.connect(DB_PATH)
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS signups(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                created_at TEXT NOT NULL   
                )""")
    conn.commit()
    conn.close()
def insert_email(email: str) -> Dict[str, Any]:
    conn = get_connection()
    cur = conn.cursor()
    try: 
        cur.execute(
        "INSERT INTO signups (email, created_at) VALUES (?, ?)",
        (email, datetime.utcnow().isoformat())
        )
        conn.commit()
        return {"inserted": True, "already_registered": False}
    except sqlite3.IntegrityError:
        return {"inserted": False, "already_registered": True}
    finally: conn.close()    
def list_signups(limit: int = 100) -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, emai, created_at FROM signups ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "email": r[1], "created_at": r[2]}
        for r in rows
    ]