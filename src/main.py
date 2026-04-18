from fastapi import FastAPI
from core.database.session import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)