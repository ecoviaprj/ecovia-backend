from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ChallengeMaster(Base):
    __tablename__ = "challenge_master"

    id = Column(Integer, primary_key=True, index=True)
    challenge_text = Column(String, nullable=False)
    option_a = Column(String(100), nullable=False)
    option_b = Column(String(100), nullable=False)
    option_c = Column(String(100), nullable=False)
    option_d = Column(String(100), nullable=False)
    correct_answer = Column(String(1), nullable=False)  
    date = Column(Date, unique=True)
    trees_awarded = Column(Integer, default=0) 

class DailyChallenge(Base):
    __tablename__ = "daily_challenges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    challenge_id = Column(Integer, ForeignKey("challenge_master.id"))
    user_answer = Column(String(1), nullable=True)      
    is_correct = Column(Boolean, default=False)      
    completed = Column(Boolean, default=False)

    user = relationship("User")
    challenge = relationship("ChallengeMaster")
