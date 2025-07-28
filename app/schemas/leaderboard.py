from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeaderboardOut(BaseModel):
    user_id: int
    score: int
    completed_all: bool
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class LeaderboardProgress(BaseModel):
    user_id: int
    progress_percent: int
    challenge_score: int
    eco_score: int
    animal_score: int
    max_score: int = 100
    class Config:
        from_attributes = True