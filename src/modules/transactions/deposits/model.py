from sqlalchemy import TIMESTAMP, Column, Integer, Numeric, String
from core.database.session import Base

class Deposit(Base):
    __tablename__ = 'deposits'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), default=function.now())