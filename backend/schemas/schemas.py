from pydantic import BaseModel
from typing import Optional, List
from pydantic.networks import EmailStr
from fastapi_users import schemas
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: EmailStr
    wallet_ids: list[int]
    
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserReadAll(UserRead):
    hashed_password: str
    registered_at: datetime

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    username: str
    password: str

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserUpdate(schemas.BaseUserUpdate):
    pass


class NewEmail(BaseModel):
    pass

class ChangeEmail(BaseModel):
    new_email: str


class ChangeEmailData(BaseModel):
    detail: str