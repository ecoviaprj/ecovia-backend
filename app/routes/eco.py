from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app import database, crud
from app.schemas import eco as eco_schemas
from typing import List, Optional, Union
from app.database import get_db
import shutil, os

router = APIRouter(
    prefix="/eco",
    tags=["Eco Tasks"]
)

@router.post("/submit", response_model=Union[eco_schemas.EcoTaskOut,dict])
def create_eco_task(task: eco_schemas.EcoTaskCreate, db: Session = Depends(database.get_db)):
    return crud.eco.create_eco_task(db, task)

@router.get("/tasks/{user_id}", response_model=list[eco_schemas.EcoTaskOut])
def get_user_tasks(user_id: int, db: Session = Depends(database.get_db)):
    return crud.eco.get_user_eco_tasks(db, user_id)

@router.post("/verify-task")
def verify_task(data: eco_schemas.EcoTaskVerify, db: Session = Depends(database.get_db)):
    return crud.eco.verify_eco_task(db, data)

@router.post("/action", response_model=eco_schemas.EcoActionOut)
def create_eco_action(action: eco_schemas.EcoActionCreate, db: Session = Depends(database.get_db)):
    return crud.eco.create_eco_action(db, action)

@router.get("/", response_model=list[eco_schemas.EcoActionOut])
def get_all_actions(db: Session = Depends(database.get_db)):
    return crud.eco.get_all_eco_actions(db)

@router.get("/eco/pending-tasks", response_model=List[eco_schemas.EcoTaskOut])
def get_pending_tasks(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.eco.get_pending_tasks(db, user_id)

