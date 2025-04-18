from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.ticket import TicketRepository
from app.repositories.message import MessageRepository
from app.schemas.ticket import TicketInDB, TicketCreate, TicketUpdate, TicketWithMessages
from app.schemas.message import MessageInDB, MessageCreate

class TicketService:
    def __init__(self, db: Session):
        self.ticket_repo = TicketRepository(db)
        self.message_repo = MessageRepository(db)

    def get_ticket(self, ticket_id: str, user_id: str) -> Optional[TicketWithMessages]:
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if not ticket or ticket.user_id != user_id:
            return None
        messages = self.message_repo.get_by_ticket(ticket_id)
        return TicketWithMessages(
            **ticket.__dict__,
            messages=[MessageInDB.from_orm(m) for m in messages]
        )

    def get_user_tickets(self, user_id: str) -> List[TicketInDB]:
        return [TicketInDB.from_orm(t) for t in self.ticket_repo.get_by_user(user_id)]

    def create_ticket(self, ticket: TicketCreate, user_id: str) -> TicketInDB:
        db_ticket = self.ticket_repo.create(ticket, user_id)
        return TicketInDB.from_orm(db_ticket)

    def update_ticket(self, ticket_id: str, update_data: TicketUpdate, user_id: str) -> Optional[TicketInDB]:
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if not ticket or ticket.user_id != user_id:
            return None
        updated_ticket = self.ticket_repo.update(ticket, update_data)
        return TicketInDB.from_orm(updated_ticket)