from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.tickets import router as tickets_router
from app.api.messages import router as messages_router
from app.db.base import Base
from app.db.session import engine

def create_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tickets_router, prefix="/tickets", tags=["tickets"])
app.include_router(messages_router, prefix="/tickets", tags=["messages"])

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/")
def read_root():
    return {"message": "Customer Support Assistant API"}