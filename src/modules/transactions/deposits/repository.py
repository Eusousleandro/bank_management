from sqlalchemy.orm import Session

from modules.transactions.deposits.model import Deposit


class DepositRepository:
    def get_deposits(db: Session):
        return db.query(Deposit).all()
    
    def get_deposit_id(db: Session, id: int):
        return db.query(Deposit).filter(Deposit.id == id).first()
    
    def create_deposit(db: Session, deposit: Deposit):
        new_deposit = Deposit(**deposit.dict())
        db.add(new_deposit)
        db.commit()
        db.refresh(new_deposit)
        return new_deposit