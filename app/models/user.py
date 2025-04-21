from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    
    tickets = relationship("Ticket", back_populates="user")