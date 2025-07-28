from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, crud
from app.schemas import leaderboard as leaderboard_schemas

router = APIRouter(
    prefix="/leaderboard",
    tags=["Leaderboard"]
)

@router.get("/", response_model=list[leaderboard_schemas.LeaderboardOut])
def get_leaderboard(db: Session = Depends(database.get_db)):
    return crud.leaderboard.get_leaderboard(db)

@router.get("/progress/{user_id}", response_model=leaderboard_schemas.LeaderboardProgress)
def get_user_progress(user_id: int, db: Session = Depends(database.get_db)):
    return crud.leaderboard.get_user_progress(db, user_id)

