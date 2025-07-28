from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app import database, crud
from app.schemas import challenge as challenge_schemas

router = APIRouter(
    prefix="/challenges",
    tags=["Daily Challenges"]
)

@router.post("/create", response_model=challenge_schemas.ChallengeMasterOut)
def create_challenge(challenge: challenge_schemas.ChallengeMasterCreate, db: Session = Depends(database.get_db)):
    return crud.challenge.create_challenge_master(db, challenge)

@router.get("/today", response_model=challenge_schemas.ChallengeMasterOut)
def get_today_challenge(db: Session = Depends(database.get_db)):
    today = date.today()
    challenge = crud.challenge.get_today_challenge(db, today)
    if not challenge:
        raise HTTPException(status_code=404, detail="No challenge for today")
    return challenge

@router.post("/submit")
def submit_challenge(data: challenge_schemas.DailyChallengeCreate, db: Session = Depends(database.get_db)):
    return crud.challenge.submit_challenge_answer(db, data)

@router.get("/history/{user_id}", response_model=list[challenge_schemas.DailyChallengeOut])
def get_user_challenge_history(user_id: int, db: Session = Depends(database.get_db)):
    return crud.challenge.get_user_challenges(db, user_id)
