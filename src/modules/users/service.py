from fastapi import HTTPException
from sqlalchemy import Session
from core.security.security import hash_password
from modules.users.mapper import to_user_response
from modules.users.repository import UserRepository
from modules.users.schema import UserBase, UserCreate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_users(self, db: Session):
        users = await self.repository.get_users(db)
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return [to_user_response(u) for u in users]
    
    async def get_user_by_id(self, db: Session, id: int):
        user = await self.repository.get_user_id(db=db, id=id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        return to_user_response(user)
    
    async def create_user(self, db: Session, user: UserCreate):
        user_existing = await  self.repository.get_user_cpf(db=db, cpf=user.cpf)
        if user_existing:
            raise HTTPException(status_code=400, detail='User with this email already exists')
        
        user.password = hash_password(user.password)
        new_user = await self.repository.create_user(db=db, user=user)
        if not new_user:
            raise HTTPException(status_code=400, detail='User could not be created')
        
        return new_user
    
    async def update_user(self, db: Session, id: int, user: UserBase):
        user_existing = await self.repository.get_user_id(db=db, id=id)
        if not user_existing:
            raise HTTPException(status_code=404, detail='User not found')
        
        user_update = await self.repository.update_user(db=db, user=user)
        if not user_update:
            raise HTTPException(status_code=400, detail='User could not be updated')
        
        return user_update

    async def delete_user(self, db: Session, id: int):
        user_existing = await self.repository.get_user_id(db=db, id=id)
        if not user_existing:
            raise HTTPException(status_code=404, detail='User not found')
        
        user_delete = await  self.repository.delete_user(db=db, id=id)
        if not user_delete:
            raise HTTPException(status_code=404, detail='User not found')
        return user_delete