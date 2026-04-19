from pydantic import BaseModel, ConfigDict


class DepositBase(BaseModel):
    pass

class DepositCreate(DepositBase):
    pass

class DepositResponse(BaseModel):
    pass

model_config = ConfigDict(from_attributes=True)