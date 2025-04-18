from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    is_ai: bool = False

class MessageInDB(MessageBase):
    id: str
    is_ai: bool
    created_at: datetime
    ticket_id: str

    class Config:
        orm_mode = True