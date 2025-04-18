from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserInDB
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(self, email: str, password: str) -> Optional[UserInDB]:
        user = self.repository.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return UserInDB.from_orm(user)

    def create_user(self, user: UserCreate) -> UserInDB:
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        db_user = self.repository.create(user)
        return UserInDB.from_orm(db_user)