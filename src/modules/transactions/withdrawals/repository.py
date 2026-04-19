from sqlalchemy.orm import Session
from modules.transactions.withdrawals.model import Withdrawal

class WithdrawalRepository:
    async def get_withdrawal(self, db: Session):
        return db.query(Withdrawal).all()
    
    async def get_withdrawal_id(self, db: Session, id: int):
        return db.query(Withdrawal).filter(Withdrawal.id == id).first()
    
    async def get_withdrawal_balance(self, db: Session):
        return db.query(Withdrawal).all()

    async def create_withdrawal(self, db: Session, withdrawal: Withdrawal):
        new_withdrawal = Withdrawal(**withdrawal.dict())
        db.add(new_withdrawal)
        db.commit()
        db.refresh(new_withdrawal)
        return new_withdrawal
        withdrawal_delete = db.query(Withdrawal).filter(Withdrawal.id == id)
        db.delele(withdrawal_delete)
        db.commit()
        return withdrawal_delete