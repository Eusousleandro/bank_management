from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.users.service import UserService
from modules.users.schema import UserCreate, UserUpdate, UserResponse
from core.auth.auth import get_current_user
from shared.dependencies import get_db

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/',  response_model=List[UserResponse])
async def get_users(
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user),
    service: UserService = Depends()):
        
        return await service.get_users(db=db)

@router.get('/{id}',  response_model=UserResponse)
async def get_user(
    id: int,
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user),
    service: UserService = Depends()):
        
        return await service.get_user_by_id(db=db, id=id)

@router.post('')
async def user_create(
        db: Session = Depends(get_db),
        user: UserCreate = Depends(),
        current_user = Depends(get_current_user),
        service: UserService = Depends()):
        
        return await service.create_user(db=db, user=user)

@router.put('/{id}')
async def user_update(
        db: Session = Depends(get_db),
        user: UserUpdate = Depends(),
        current_user = Depends(get_current_user),
        service: UserService = Depends()):
        
        return await service.update_user(db=db, id=id, user=user)

@router.delete('/{id}')
async def user_delete(
        id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user),
        service: UserService = Depends()):
        
        return await service.delete_user(db=db, id=id)