from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, ticket_id: str) -> Optional[Ticket]:
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def get_by_user(self, user_id: str) -> List[Ticket]:
        return self.db.query(Ticket).filter(Ticket.user_id == user_id).all()

    def create(self, ticket: TicketCreate, user_id: str) -> Ticket:
        db_ticket = Ticket(**ticket.dict(), user_id=user_id)
        self.db.add(db_ticket)
        self.db.commit()
        self.db.refresh(db_ticket)
        return db_ticket

    def update(self, ticket: Ticket, update_data: TicketUpdate) -> Ticket:
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(ticket, field, value)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket