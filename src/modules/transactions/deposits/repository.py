from sqlalchemy.orm import Session

from modules.transactions.deposits.model import Deposit


class DepositRepository:
    async def get_deposits(self, db: Session):
        return db.query(Deposit).all()
    
    async def get_deposit_id(self, db: Session, id: int):
        return db.query(Deposit).filter(Deposit.id == id).first()
    
    async def create_deposit(self, db: Session, deposit: Deposit):
        new_deposit = Deposit(**deposit.dict())
        db.add(new_deposit)
        db.commit()
        db.refresh(new_deposit)
        return new_deposit