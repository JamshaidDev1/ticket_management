from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.message import MessageInDB, MessageCreate
from app.services.message import MessageService
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/{ticket_id}/messages", response_model=List[MessageInDB])
def get_messages(
    ticket_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = MessageService(db)
    return service.get_ticket_messages(ticket_id, current_user)

@router.post("/{ticket_id}/messages", response_model=MessageInDB, status_code=status.HTTP_201_CREATED)
def create_message(
    ticket_id: str,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    service = MessageService(db)
    return service.create_message(message, ticket_id, current_user)