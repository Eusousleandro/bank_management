from sqlalchemy import Column, Integer, String
from core.database.session import Base

class Deposit(Base):
    __tablename__ = 'deposits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    value = Column(String(20), nullable=False)