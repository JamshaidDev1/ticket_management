from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.message import MessageRepository
from app.repositories.ticket import TicketRepository
from app.schemas.message import MessageInDB, MessageCreate

class MessageService:
    def __init__(self, db: Session):
        self.message_repo = MessageRepository(db)
        self.ticket_repo = TicketRepository(db)

    def get_ticket_messages(self, ticket_id: str, user_id: str) -> List[MessageInDB]:
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if not ticket or ticket.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )
        messages = self.message_repo.get_by_ticket(ticket_id)
        return [MessageInDB.from_orm(m) for m in messages]

    def create_message(self, message: MessageCreate, ticket_id: str, user_id: str) -> MessageInDB:
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if not ticket or ticket.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )
        db_message = self.message_repo.create(message, ticket_id)
        return MessageInDB.from_orm(db_message)