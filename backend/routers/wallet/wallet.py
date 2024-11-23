from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, wallet, transaction 
from ...schemas import NewWallet, ResponseDetail
from ...dependencies import current_user
from typing import Dict
from ...details import *

wallet_router = APIRouter(
    prefix = "/wallet",
    tags = ["wallet_ops"]
)

@wallet_router.post(
    "/add",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully created category"},
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_NOT_FOUND}
                }
            }
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}
                }
            }
        }
    }
)
async def add_new_wallet(
        wallet_data: NewWallet, 
        session: AsyncSession = Depends(get_async_session)
    ):
    
    query = insert(wallet).values(
        name = wallet_data.name,
        user_id = wallet_data.user_id
    )

    if wallet_data.balance is not None:
        query = query.values(balance = wallet_data.balance)

    try:
        await session.execute(query)
        await session.commit()

        return {"detail": OK}

    except IntegrityError:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_OR_TRANSACTION_NOT_FOUND,   
        )
