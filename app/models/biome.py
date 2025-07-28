from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost_trees = Column(Integer)
    cost_coins = Column(Integer)

class UserAnimal(Base):
    __tablename__ = "user_animals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    animal_id = Column(Integer, ForeignKey("animals.id"))

    user = relationship("User")
    animal = relationship("Animal")
