from modules.users.model import User
from modules.users.schema import UserResponse

def to_user_response(user: User) -> UserResponse:
    return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
        )