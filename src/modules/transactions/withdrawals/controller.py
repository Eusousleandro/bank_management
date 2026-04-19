from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.auth.auth import get_current_user
from modules.transactions.withdrawals.schema import WithdrawalCreate, WithdrawalResponse, WithdrawalUpdate
from modules.transactions.withdrawals.service import WithdrawalService
from shared.dependencies import get_db

router = APIRouter(prefix='/withdrawal', tags=['Withdrawal'])

@router.get('/', response_model=List[WithdrawalResponse])
async def get_withdrawal(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    service: WithdrawalService = Depends()
):
    return await service.get_withdrawals(db=db)

@router.get('/{id}', response_model=WithdrawalResponse)
async def get_withdrawal_id(
        id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user),
        service: WithdrawalService = Depends()
):
    return await service.get_withdrawal_id(db=db, id=id)

@router.post('/')
async def withdrawal_create(
    withdrawal: WithdrawalCreate,
    db: Session =  Depends(get_db),
    current_user = Depends(get_current_user),
    service: WithdrawalService = Depends()
):
    return await service.create_withdrawal(db=db, withdrawal=withdrawal)