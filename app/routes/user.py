from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, crud
from app.schemas import user as user_schemas


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=user_schemas.UserOut)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.user.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=user_schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.user.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=user_schemas.UserOut)
def update_user(user_id: int, update: user_schemas.UserUpdate, db: Session = Depends(database.get_db)):
    return crud.user.update_user(db, user_id, update)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    crud.user.delete_user(db, user_id)
    return {"message": "User deleted"}
