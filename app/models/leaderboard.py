from sqlalchemy import Boolean, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class LeaderboardEntry(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, default=0)
    completed_all = Column(Boolean, default=False)
    completed_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
