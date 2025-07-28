from pydantic import BaseModel
from typing import Optional
import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    avatar_name: str
    onboarding_time: Optional[datetime.datetime] = None

class UserUpdate(BaseModel):
    total_trees: Optional[int]
    total_eco_coins: Optional[int]

class UserOut(UserBase):
    id: int
    avatar_name: str
    total_trees: int
    total_eco_coins: int

    class Config:
        from_attributes = True
