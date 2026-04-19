from fastapi import Depends
from sqlalchemy.orm import Session

from modules.transactions.deposits.mapper import to_deposit_response
from modules.transactions.deposits.repository import DepositRepository
from modules.transactions.deposits.schema import DepositCreate
from shared.exceptions import not_found


class DepositService:
    def __init__(self, repository: DepositRepository = Depends()):
        self.repository = repository

    async def get_deposits(self, db: Session):
        deposits = await self.repository.get_deposits(db)
        if not deposits: 
            raise not_found()
        
        return [to_deposit_response(d) for d in deposits]
    
    async def get_deposit_id(self, db: Session, id: int):
        deposit = await self.repository.get_deposit_id(db=db, id=id)
        if not deposit:
            raise not_found()
        
        return to_deposit_response(deposit)
    
    async def deposit_create(self, db: Session, deposit: DepositCreate):
        new_deposit = await self.repository.create_deposit(db=db, deposit=deposit)
        if not new_deposit:
            raise not_found()
        
        return new_deposit