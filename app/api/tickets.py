from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.ticket import TicketInDB, TicketCreate, TicketUpdate, TicketWithMessages
from app.schemas.message import MessageInDB, MessageCreate
from app.services.ticket import TicketService
from app.services.message import MessageService
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[TicketInDB])
def get_tickets(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = TicketService(db)
    return service.get_user_tickets(current_user)

@router.post("/", response_model=TicketInDB, status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = TicketService(db)
    return service.create_ticket(ticket, current_user)

@router.get("/{ticket_id}", response_model=TicketWithMessages)
def get_ticket(
    ticket_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = TicketService(db)
    ticket = service.get_ticket(ticket_id, current_user)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    return ticket

@router.put("/{ticket_id}", response_model=TicketInDB)
def update_ticket(
    ticket_id: str,
    ticket: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = TicketService(db)
    updated_ticket = service.update_ticket(ticket_id, ticket, current_user)
    if not updated_ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    return updated_ticket

@router.post("/{ticket_id}/messages", response_model=MessageInDB, status_code=status.HTTP_201_CREATED)
def create_message(
    ticket_id: str,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    message_service = MessageService(db)
    return message_service.create_message(ticket_id, message, current_user)

@router.get("/{ticket_id}/ai-response")
async def get_ai_response(
    ticket_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    ticket_service = TicketService(db)
    ticket = ticket_service.get_ticket(ticket_id, current_user)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    
    async def event_stream():
        # Implement your AI response streaming logic here
        yield "data: AI response streaming not implemented yet\n\n"
    
    return EventSourceResponse(event_stream())