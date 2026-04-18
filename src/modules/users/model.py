from sqlalchemy import Integer, Column, String

class User:
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    cpf = Column(String(11), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False) 