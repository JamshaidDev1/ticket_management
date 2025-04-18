from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class UserRole(str, PyEnum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    
    tickets = relationship("Ticket", back_populates="user")