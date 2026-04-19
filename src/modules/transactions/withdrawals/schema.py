from pydantic import BaseModel, ConfigDict


class WithdrawalBase(BaseModel):
    balance: str

class WithdrawalCreate(WithdrawalBase):
    pass

class WithdrawalUpdate(BaseModel):
    pass

class WithdrawalResponse(BaseModel):
    pass

model_config = ConfigDict(from_attributes=True)