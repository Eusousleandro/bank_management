from datetime import datetime
from pydantic import BaseModel, ConfigDict


class WithdrawalBase(BaseModel):
    amount: float
    timestamp: datetime

class WithdrawalCreate(WithdrawalBase):
    pass

class WithdrawalResponse(BaseModel):
    user_id: int
    amount: float

model_config = ConfigDict(from_attributes=True)