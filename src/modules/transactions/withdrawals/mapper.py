from modules.transactions.withdrawals.model import Withdrawal
from modules.transactions.withdrawals.schema import WithdrawalResponse

def to_withdrawal_response(withdrawal: Withdrawal) -> WithdrawalResponse:
    return WithdrawalResponse (
        id=withdrawal.id,
        user=withdrawal.user_id,
        name=withdrawal.name,
        amount=withdrawal.amount,
        timestamp=withdrawal.timestamp
    )