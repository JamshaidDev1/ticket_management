from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Message(Base):
    content = Column(String, nullable=False)
    is_ai = Column(Boolean, default=False, nullable=False)
    ticket_id = Column(String, ForeignKey("ticket.id"), nullable=False)
    
    ticket = relationship("Ticket", back_populates="messages")