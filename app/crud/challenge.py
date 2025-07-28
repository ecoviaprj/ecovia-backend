from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.crud.leaderboard import update_leaderboard_entry
from app.utils.user_utils import get_existing_user


def create_challenge_master(db: Session, challenge: schemas.ChallengeMasterCreate):
    existing_challenge = db.query(models.ChallengeMaster).filter(models.ChallengeMaster.date == challenge.date).first()
    if existing_challenge:
        raise HTTPException(status_code=400, detail="Challenge for this date already exists")

    db_challenge = models.ChallengeMaster(**challenge.dict())
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge

def get_today_challenge(db: Session, date):
    return db.query(models.ChallengeMaster).filter(models.ChallengeMaster.date == date).first()

def submit_challenge_answer(db: Session, data: schemas.DailyChallengeCreate):
    challenge = db.query(models.ChallengeMaster).filter(models.ChallengeMaster.id == data.challenge_id).first()
    user = db.query(models.User).filter(models.User.id == data.user_id).first()

    if not challenge or not user:
        raise HTTPException(status_code=404, detail="User or Challenge not found")

    existing = db.query(models.DailyChallenge).filter_by(user_id=data.user_id, challenge_id=data.challenge_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Challenge already answered")

    is_correct = (data.user_answer.strip().lower() == challenge.correct_answer.strip().lower())
    trees_awarded = challenge.trees_awarded if is_correct else 0

    db_entry = models.DailyChallenge(
        user_id=data.user_id,
        challenge_id=data.challenge_id,
        user_answer=data.user_answer,
        is_correct=is_correct,
        completed=True
    )
    db.add(db_entry)

    if is_correct:
        user.total_trees += trees_awarded

    db.commit()

    update_leaderboard_entry(db, data.user_id)

    return {
        "message": "Answer submitted",
        "is_correct": is_correct,
        "trees_awarded": trees_awarded
    }

def get_user_challenges(db: Session, user_id: int):
    get_existing_user(db, user_id)
    return db.query(models.DailyChallenge).filter(models.DailyChallenge.user_id == user_id).all()
