from pydantic import BaseModel
from typing import Optional, List
from pydantic.networks import EmailStr
from fastapi_users import schemas
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: EmailStr
    
    is_active: bool = False
    is_superuser: bool = False
    is_verified: bool = False


class UserReadAll(UserRead):
    hashed_password: str
    registered_at: datetime

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    username: str
    password: str

    is_active: Optional[bool] = False
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserUpdate(schemas.BaseUserUpdate):
    pass

class NewCategory(BaseModel):
    name: str
    is_income: bool

class ReadCategory(NewCategory):
    id: int

class UpdateCategory(BaseModel):
    id: int
    name: str | None = None
    is_income: bool | None = None

class ResponseDetail(BaseModel):
    detail: str

class NewTransaction(BaseModel):
    title: str
    category_id: int
    wallet_id: int
    amount: float
    date: datetime

class NewWallet(BaseModel):
    name: str
    balance: float | None = None
    user_id: int
    
class RemoveWallet(BaseModel):
    id: int
    
class UpdateWallet(BaseModel):
    id: int
    name: str | None = None
    balance: float | None = None    
    user_id: int | None = None

class UpdateTransaction(BaseModel):
    id: int
    title: str | None = None
    category_id: int | None = None
    amount: float | None = None
    date: datetime | None = None

class ReadTransaction(BaseModel):
    id: int
    title: str
    category_id: int
    wallet_id: int
    amount: float
    date: datetime

class GetTransaction(BaseModel):
    wallet_id: int
    start: datetime
    end: datetime
    
class UserWalletId(BaseModel):
    user_id: int

class ReadWallet(BaseModel):
    id: int
    name: str
    balance: float
    user_id: int

class WhalletId(BaseModel):
    id: int

class GeminiResponse(BaseModel):
    detail: str

class GetGeminiRecomendation(BaseModel):
    wallet_id: int
