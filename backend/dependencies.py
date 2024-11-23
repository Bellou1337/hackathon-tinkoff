from .auth import fastapi_users

current_user = fastapi_users.current_user()

current_superuser = fastapi_users.current_user(
    superuser=True
)