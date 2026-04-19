from pydantic import BaseModel, ConfigDict, PositiveFloat

class UserBase(BaseModel):
    name: str
    cpf: str
    password: str
    balance: PositiveFloat

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: str | None
    cpf: str | None
    password: str | None

class UserResponse(BaseModel):
    id: int
    name: str
    cpf: str
    amount: float

model_config = ConfigDict(from_attributes=True)