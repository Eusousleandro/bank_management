from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from core.database.session import Base

class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), default=function.now())