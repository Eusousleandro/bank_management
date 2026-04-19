from sqlalchemy.orm import Session
from modules.users.model import User
from modules.users.schema import UserUpdate

class UserRepository:
    async def get_users(self, db: Session):
        return db.query(User).all()

    async def get_user_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    async def get_user_cpf(self, db: Session, cpf: str):
        return db.query(User).filter(User.cpf == cpf).first()

    async def create_user(self, db: Session, user: User):
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    async def update_user(db: Session, user: UserUpdate):
        user_update = db.query(User).filter(User.id == id)
        user_data = user.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(user_update, key, value)
        
        db.commit()
        db.refresh(user_update)
        return user_update

    async def delete_user(db: Session, id: int):
        user_delete = db.query(User).filter(User.id == id)
        db.delete(user_delete)
        db.commit()
        return user_delete