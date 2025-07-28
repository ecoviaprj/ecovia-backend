from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.crud.leaderboard import update_leaderboard_entry
from typing import Optional
from app.utils.user_utils import get_existing_user
import os
from datetime import date

def create_eco_task(db: Session, task: schemas.EcoTaskCreate):
    get_existing_user(db, task.user_id)

    existing = db.query(models.EcoTask).filter_by(
        user_id=task.user_id,
        task_id=task.task_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already submitted this task.")
    
    task_data=task.dict()
    task_data["date_assigned"]=task_data.get("date_assigned")or date.today()
    task_data["status"]="pending"
    db_task=models.EcoTask(**task_data)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_user_eco_tasks(db: Session, user_id: int):
    get_existing_user(db, user_id)
    return db.query(models.EcoTask).filter(models.EcoTask.user_id == user_id).all()

def verify_eco_task(db: Session, data: schemas.EcoTaskVerify):
    task = db.query(models.EcoTask).get(data.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    user = db.query(models.User).get(task.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    action = db.query(models.EcoAction).get(task.task_id)
    if not action:
        raise HTTPException(status_code=404, detail="Related eco action not found")

    task.status = data.status

    eco_coins_awarded = 0
    if data.status == "verified":
        user.total_eco_coins += action.eco_coins
        eco_coins_awarded = action.eco_coins

    db.commit()
    update_leaderboard_entry(db, user.id)

    return {
        "message": f"Task {data.status}",
        "eco_coins_awarded": eco_coins_awarded
    }


def create_eco_action(db: Session, action: schemas.EcoActionCreate):
    db_action = models.EcoAction(**action.dict())
    db.add(db_action)
    db.commit()
    db.refresh(db_action)
    return db_action

def get_all_eco_actions(db: Session):
    return db.query(models.EcoAction).all()

def get_pending_tasks(db: Session, user_id: Optional[int] = None):
    if user_id is not None:
        get_existing_user(db, user_id)
    query = db.query(models.EcoTask).filter(models.EcoTask.status == "pending")
    if user_id:
        query = query.filter(models.EcoTask.user_id == user_id)
    return query.all()
