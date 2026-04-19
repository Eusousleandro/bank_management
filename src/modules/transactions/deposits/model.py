from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, Numeric, String, func
from core.database.session import Base

class Deposit(Base):
    __tablename__ = 'deposits'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('deposits.id'), nullable=False)
    name = Column(String(250), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), default=func.now())