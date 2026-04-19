from sqlalchemy import Column, Integer, Numeric, String, TIMESTAMP
from core.database.session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    cpf = Column(String(11), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False) 
    amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=function.now())