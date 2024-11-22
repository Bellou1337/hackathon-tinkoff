from backend.config import config
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import AsyncGenerator
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends
from sqlalchemy import Integer, Column, String, TIMESTAMP, Boolean, ARRAY
from datetime import datetime
from ..config import config
from sqlalchemy.orm import DeclarativeBase



DATABASE_URL =  f"postgresql+asyncpg://{config['Database']['DB_USER']}:{config['Database']['DB_PASS']}@{config['Database']['DB_HOST']}:{config['Database']['DB_PORT']}/{config['Database']['DB_NAME']}"

class Base(DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    wallet_ids = Column(ARRAY(Integer))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
