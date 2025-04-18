from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from uuid import uuid4

@as_declarative()
class Base:
    id = Column(str, primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()