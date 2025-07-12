from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import ESP32Data
from database import SessionLocal



router = APIRouter()

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.post("/log/")
def log_data(payload: ESP32Data, database: Session = Depends(get_database)):
    log = User(esp32_data=payload.data)
    database.add(log)
    database.commit()
    return {"status":"success"}
