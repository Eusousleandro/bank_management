from sqlalchemy.orm import Session

from modules.transactions.withdrawals.model import Withdrawal
from modules.transactions.withdrawals.schema import WithdrawalBase, WithdrawalUpdate


class WithdrawalRepository:
    def get_withdrawal(db: Session):
        return db.query(Withdrawal).all()
    
    def get_withdrawal_id(db: Session, id: int):
        return db.query(Withdrawal).filter(Withdrawal.id == id).first()
    
    def get_withdrawal_balance(db: Session, balance: Withdrawal):
        return db.query(Withdrawal).filter(Withdrawal.balance == balance)

    def create_withdrawal(db: Session, withdrawal: Withdrawal):
        new_withdrawal = Withdrawal(**withdrawal.dict())
        db.add(new_withdrawal)
        db.commit()
        db.refresh(new_withdrawal)
        return new_withdrawal
    
    def update_withdrawal(db: Session, id: int, withdrawal: WithdrawalUpdate):
        withdrawal_update = db.query(Withdrawal).filter(Withdrawal.id == id)
        withdrawal_data = withdrawal.model_dump(exclude_unset=True)
         
        for key, value in withdrawal_data.items():
            setattr(withdrawal_update, key, value)
        
        db.commit()
        db.refresh(withdrawal_update)
        return withdrawal_update
    
    def delete_withdrawal(db: Session, id: int):
        withdrawal_delete = db.query(Withdrawal).filter(Withdrawal.id == id)
        db.delele(withdrawal_delete)
        db.commit()
        return withdrawal_delete