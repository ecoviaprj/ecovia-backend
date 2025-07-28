from pydantic import BaseModel
from typing import List

class AnimalBase(BaseModel):
    name: str
    cost_trees: int
    cost_coins: int

class AnimalCreate(AnimalBase):
    pass

class AnimalOut(AnimalBase):
    id: int

    class Config:
        from_attributes = True

class UserAnimalCreate(BaseModel):
    user_id: int
    animal_id: int

class UserAnimalOut(BaseModel):
    id: int
    user_id: int
    animal: AnimalOut

    class Config:
        from_attributes = True
