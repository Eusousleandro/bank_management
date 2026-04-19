from modules.transactions.deposits.model import Deposit
from modules.transactions.deposits.schema import DepositResponse

def to_deposit_response(deposit: Deposit) -> DepositResponse:
    return DepositResponse(
        id=deposit.id,
        user=deposit.user_id,
        name=deposit.name,
        amount=deposit.amount,
        timestamp=deposit.timestamp
    )