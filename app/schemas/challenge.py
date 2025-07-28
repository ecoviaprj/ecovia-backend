from pydantic import BaseModel
from datetime import date
from typing import Optional

class ChallengeMasterCreate(BaseModel):
    challenge_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str     
    date: date
    trees_awarded: int   

class ChallengeMasterOut(BaseModel):
    id: int
    challenge_text: str
    correct_answer: str
    date: date
    trees_awarded: int

    class Config:
        from_attributes = True

class DailyChallengeCreate(BaseModel):
    user_id: int
    challenge_id: int
    user_answer: str        
    
class DailyChallengeOut(BaseModel):
    id: int
    user_id: int
    challenge: ChallengeMasterOut
    user_answer: Optional[str]
    is_correct: Optional[bool]
    completed: bool

    class Config:
        from_attributes = True
