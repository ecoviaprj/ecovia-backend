from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models
from app.crud.leaderboard import update_leaderboard_entry
from app.utils.user_utils import get_existing_user


def get_all_animals(db: Session):
    return db.query(models.Animal).all()

def get_user_animals(db: Session, user_id: int):
    get_existing_user(db, user_id)
    return db.query(models.UserAnimal).filter(models.UserAnimal.user_id == user_id).all()

def buy_animal(db: Session, user_id: int, animal_id: int):
    animal = db.query(models.Animal).get(animal_id)
    user = db.query(models.User).get(user_id)

    if not animal or not user:
        raise HTTPException(status_code=404, detail="User or animal not found")

    if user.total_trees < animal.cost_trees or user.total_eco_coins < animal.cost_coins:
        raise HTTPException(status_code=400, detail="Insufficient trees or eco coins")


    existing = db.query(models.UserAnimal).filter_by(user_id=user_id, animal_id=animal_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Animal already purchased")


    user.total_trees -= animal.cost_trees
    user.total_eco_coins -= animal.cost_coins


    user_animal = models.UserAnimal(user_id=user_id, animal_id=animal_id)
    db.add(user_animal)
    db.commit()


    update_leaderboard_entry(db, user_id)

    return {"message": "Animal purchased successfully"}
