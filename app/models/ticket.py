from sqlalchemy import Column, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="tickets")
    messages = relationship("Message", back_populates="ticket")