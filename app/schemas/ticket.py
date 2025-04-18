from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class TicketBase(BaseModel):
    title: str
    description: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TicketStatus]

class TicketInDB(TicketBase):
    id: str
    status: TicketStatus
    created_at: datetime
    user_id: str

    class Config:
        orm_mode = True

class TicketWithMessages(TicketInDB):
    messages: List["MessageInDB"]