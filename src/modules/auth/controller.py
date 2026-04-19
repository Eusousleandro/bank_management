from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from modules.auth.schema import Login, TokenResponse
from modules.auth.service import LoginService
from shared.dependencies import get_db

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('', response_model=TokenResponse)
async def login(
    db: Session = Depends(get_db),
    service: LoginService = Depends()
):
    login = Login(
        
    )
    return await service.auth_user(db=db, login=login)


