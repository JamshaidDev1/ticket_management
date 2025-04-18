from sqlalchemy import Column, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class TicketStatus(str, PyEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Ticket(Base):
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)
    
    user = relationship("User", back_populates="tickets")
    messages = relationship("Message", back_populates="ticket")