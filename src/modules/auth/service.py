from fastapi import Depends
from sqlalchemy.orm import Session

from core.auth.auth import create_access_token
from modules.auth.schema import Login
from modules.users.repository import UserRepository
from shared.exceptions import not_found


class LoginService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    async def auth_user(self, db: Session, login: Login):
        user = await self.repository.get_user_cpf(db=db, cpf=login.cpf)
        if not user:
            raise not_found()
        
        token = create_access_token({'sub': user.cpf})
        return {'access_token': token, 'token_type': 'bearer'}