from fastapi import Depends
from sqlalchemy.orm import Session

from modules.transactions.withdrawals.mapper import to_withdrawal_response
from modules.transactions.withdrawals.repository import WithdrawalRepository
from modules.transactions.withdrawals.schema import WithdrawalCreate
from shared.exceptions import not_found


class WithdrawalService:
    def __init__(self, repository: WithdrawalRepository = Depends()):
        self.repository = repository

    async def get_withdrawals(self, db: Session):
        withdrawals = await self.repository.get_withdrawal(db)
        if not withdrawals:
            raise not_found('Withdrawals')
        
        return [to_withdrawal_response(w) for w in withdrawals]
    
    async def get_withdrawal_id(self, db: Session, id: int):
        withdrawal = await self.repository.get_withdrawal_id(db=db, id=id)
        if not withdrawal:
            raise not_found('Withdrawal')
        
        return to_withdrawal_response(withdrawal)
    
    async def create_withdrawal(self, db: Session, withdrawal: WithdrawalCreate):
        balance_existing = await self.repository.get_withdrawal_balance(db=db, withdrawal=withdrawal)
        if balance_existing < withdrawal:
            raise not_found('Withdrawal')
        
        new_withdrawal = await self.repository.create_withdrawal(db=db, withdrawal=withdrawal)
        if not new_withdrawal: 
            raise not_found('Withdrawal')
        
        return new_withdrawal