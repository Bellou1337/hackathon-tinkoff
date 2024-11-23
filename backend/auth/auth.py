from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users import FastAPIUsers

from ..database.database import User
from .manager import get_user_manager
from ..config import config

SECRET = config['Miscellaneous']['Secret']
TOKEN_EXPIRE = config.get("Miscellaneous", "token_expire")

transport = BearerTransport("auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=TOKEN_EXPIRE)



auth_backend = AuthenticationBackend(
    name="auth",
    transport=transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)