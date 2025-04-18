from typing import List
from sqlalchemy.orm import Session
from app.models.message import Message
from app.schemas.message import MessageCreate

class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_ticket(self, ticket_id: str) -> List[Message]:
        return self.db.query(Message).filter(Message.ticket_id == ticket_id).all()

    def create(self, message: MessageCreate, ticket_id: str) -> Message:
        db_message = Message(**message.dict(), ticket_id=ticket_id)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message