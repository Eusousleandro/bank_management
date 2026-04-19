from fastapi import FastAPI
from core.database.session import Base, engine
from modules.users.controller import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)