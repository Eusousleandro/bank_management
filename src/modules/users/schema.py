from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    cpf: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: str | None
    cpf: str | None
    password: str | None

model_config = ConfigDict(from_attributes=True)