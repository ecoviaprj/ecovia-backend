from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database,crud 
from app.schemas import biome as biome_schemas


router = APIRouter(
    prefix="/biome",
    tags=["Biome"]
)

@router.get("/shop", response_model=list[biome_schemas.AnimalOut])
def get_all_animals(db: Session = Depends(database.get_db)):
    return crud.biome.get_all_animals(db)

@router.post("/buy")
def buy_animal(data: biome_schemas.UserAnimalCreate, db: Session = Depends(database.get_db)):
    return crud.biome.buy_animal(db, data.user_id, data.animal_id)

@router.get("/my-animals/{user_id}", response_model=list[biome_schemas.UserAnimalOut])
def get_user_animals(user_id: int, db: Session = Depends(database.get_db)):
    return crud.biome.get_user_animals(db, user_id)
