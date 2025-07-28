from sqlalchemy.orm import Session
from app import models
from datetime import datetime
from app.utils.user_utils import get_existing_user


def get_leaderboard(db: Session, limit: int = 10):
    return (
        db.query(models.LeaderboardEntry)
        .order_by(models.LeaderboardEntry.score.desc(), models.LeaderboardEntry.completed_at.asc())
        .limit(limit)
        .all()
    )

def update_leaderboard_entry(db: Session, user_id: int):
    user = db.query(models.User).get(user_id)
    if not user:
        return
    challenges_completed = db.query(models.DailyChallenge).filter_by(user_id=user_id, is_correct=True).count()
    eco_tasks_verified = db.query(models.EcoTask).filter_by(user_id=user_id, status="verified").count()
    animals_bought = db.query(models.UserAnimal).filter_by(user_id=user_id).count()

    challenges_completed = min(challenges_completed, 30)
    eco_tasks_verified = min(eco_tasks_verified, 3)
    animals_bought = min(animals_bought, 4)

    challenge_score = challenges_completed * 1     
    eco_score = eco_tasks_verified * 10            
    animal_score = animals_bought * 10             

    total_score = challenge_score + eco_score + animal_score

    completed_all = (
        challenges_completed == 30 and
        eco_tasks_verified == 3 and
        animals_bought == 4
    )

    entry = db.query(models.LeaderboardEntry).filter_by(user_id=user_id).first()
    if not entry:
        entry = models.LeaderboardEntry(user_id=user_id)

    entry.score = total_score
    entry.completed_all = completed_all
    if completed_all:
        entry.completed_at = datetime.utcnow()

    db.add(entry)
    db.commit()


def get_user_progress(db: Session, user_id: int):
    get_existing_user(db, user_id)

    challenges_completed = db.query(models.DailyChallenge).filter_by(user_id=user_id, is_correct=True).count()
    eco_tasks_verified = db.query(models.EcoTask).filter_by(user_id=user_id, status="verified").count()
    animals_bought = db.query(models.UserAnimal).filter_by(user_id=user_id).count()

    challenges_completed = min(challenges_completed, 30)
    eco_tasks_verified = min(eco_tasks_verified, 3)
    animals_bought = min(animals_bought, 4)

    challenge_score = challenges_completed * 1         
    eco_score = eco_tasks_verified * 10                
    animal_score = animals_bought * 10                 

    progress_percent = challenge_score + eco_score + animal_score

    return {
        "user_id": user_id,
        "progress_percent": progress_percent,
        "challenge_score": challenge_score,
        "eco_score": eco_score,
        "animal_score": animal_score,
        "max_score": 100
    }

