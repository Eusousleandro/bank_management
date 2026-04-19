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

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

model_config = ConfigDict(from_attributes=True)