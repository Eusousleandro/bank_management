from sqlalchemy import Column, ForeignKey, Integer, Numeric, TIMESTAMP, String, func
from core.database.session import Base

class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('withdrawals.id'), nullable=False)
    name = Column(String(250), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), default=func.now())