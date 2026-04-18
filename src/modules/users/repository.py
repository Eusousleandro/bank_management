from sqlalchemy import Session
from modules.users.model import User
from modules.users.schema import UserUpdate

class UserRepository:
    def get_users(db: Session):
        return db.query(User).all()

    def get_user_id(db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def get_user_cpf(db: Session, cpf: str):
        return db.query(User).filter(User.cpf == cpf).first()

    def create_user(db: Session, user: User):
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def update_user(db: Session, user: UserUpdate):
        user_update = db.query(User).filter(User.id == id)
        user_data = user.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(user_update, key, value)
        
        db.commit()
        db.refresh(user_update)

    def delete_user(db: Session, id: int):
        user_delete = db.query(User).filter(User.id == id)
        db.delete(user_delete)
        db.commit()
        return user_delete