from sqlalchemy import Column, Integer, String
from core.database.session import Base

class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(String(50), nullable=False)
    value = Column(String(20), nullable=False)