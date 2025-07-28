from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class TaskStatusEnum(str, Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"

class EcoTaskBase(BaseModel):
    user_id: int
    task_id: int
    task_name: str
    image_path: str
    date_assigned: date

class EcoTaskCreate(EcoTaskBase):
    pass

class EcoTaskOut(EcoTaskBase):
    id: int
    status: TaskStatusEnum

    class Config:
        orm_mode = True

class EcoTaskVerify(BaseModel):
    task_id: int
    status: TaskStatusEnum

class EcoActionBase(BaseModel):
    title: str
    description: str
    eco_coins: int
    level: int

class EcoActionCreate(EcoActionBase):
    pass

class EcoActionOut(EcoActionBase):
    id: int

    class Config:
        orm_mode = True
