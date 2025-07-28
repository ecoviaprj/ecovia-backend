from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    avatar_name = Column(String)
    total_trees = Column(Integer, default=0)
    total_eco_coins = Column(Integer, default=0)
    onboarding_time = Column(DateTime, default=datetime.utcnow)
    eco_tasks = relationship("EcoTask", back_populates="user")