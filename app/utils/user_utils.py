from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models

def get_existing_user(db: Session, user_id: int) -> models.User:
    user = db.query(models.User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user
