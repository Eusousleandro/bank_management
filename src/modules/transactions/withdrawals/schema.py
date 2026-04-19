from pydantic import BaseModel


class WithdrawalBase(BaseModel):
    balance: str

class WithdrawalCreate(WithdrawalBase):
    pass

class WithdrawalUpdate(BaseModel):
    pass

class WithdrawalResponse(BaseModel):
    pass