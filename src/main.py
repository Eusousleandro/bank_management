from fastapi import FastAPI

from core.database.session import Base, engine
from modules.auth.controller import router as auth_router
from modules.users.controller import router as user_router
from modules.transactions.deposits.controller import router as deposit_router
from modules.transactions.withdrawals.controller import router as withdrawal_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(deposit_router)
app.include_router(withdrawal_router)