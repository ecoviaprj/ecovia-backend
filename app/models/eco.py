from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import date

class TaskStatusEnum(str, enum.Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"

class EcoTask(Base):
    __tablename__ = "eco_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("eco_actions.id"))
    task_name = Column(String(100))
    image_path = Column(String(255))
    status = Column(Enum(TaskStatusEnum))
    date_assigned = Column(Date)

    user = relationship("User", back_populates="eco_tasks")
    eco_action = relationship("EcoAction")
    
class EcoAction(Base):
    __tablename__ = "eco_actions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(255))
    eco_coins = Column(Integer)
    level = Column(Integer, default=1)
    created_at = Column(Date, default=date.today)

