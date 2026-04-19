from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.auth.auth import get_current_user
from modules.transactions.deposits.schema import DepositCreate, DepositResponse
from modules.transactions.deposits.service import DepositService
from shared.dependencies import get_db

router = APIRouter(prefix='/deposits', tags=['Deposits'])

@router.get('/', response_model=List[DepositResponse])
async def get_deposits(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    service: DepositService = Depends()
):
    
    return await service.get_deposits(db=db)

@router.get('/{id}', response_model=DepositResponse)
async def get_deposit_id(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    service: DepositService = Depends()
):
    
    return await service.get_deposit_id(db=db, id=id)

@router.post('/')
async def create_deposit(
    deposit: DepositCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    service: DepositService = Depends()
):

    return await service.deposit_create(db=db, deposit=deposit)