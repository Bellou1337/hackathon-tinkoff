from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, wallet, transaction 
from ...schemas import NewWallet, ResponseDetail, RemoveWallet,UpdateWallet
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
        200: {"model": ResponseDetail, "description": "Successfully created wallet"},
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

@wallet_router.post(
    "/remove_wallet",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully removed wallet"},
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}},},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def remove_wallet(wallet_data: RemoveWallet,session: AsyncSession = Depends(get_async_session)):
    
    try:
        stmt = select(wallet).where(wallet.c.id == wallet_data.id)
        result = await session.execute(stmt)
        
        if not result.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=WALLET_NOT_FOUND
            )
        
        query = delete(wallet).where(wallet.c.id == wallet_data.id)
        await session.execute(query)
        await session.commit()

        return {"detail": OK}

    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=SERVER_ERROR_SOMETHING_WITH_THE_DATA
        )

@wallet_router.post(
    "/update_wallet",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully updated wallet"},
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def update_wallet(wallet_data: UpdateWallet,session: AsyncSession = Depends(get_async_session)):

    try:
        stmt = select(wallet).where(wallet.c.id == wallet_data.id)
        result = await session.execute(stmt)

        if not result.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=WALLET_NOT_FOUND)

        update_values = {}
        if wallet_data.name is not None:
            update_values["name"] = wallet_data.name
        if wallet_data.balance is not None:
            update_values["balance"] = wallet_data.balance
        if wallet_data.user_id is not None:
            update_values["user_id"] = wallet_data.user_id
        
        query = update(wallet).where(wallet.c.id == wallet_data.id).values(**update_values)
        await session.execute(query)
        await session.commit()
        
        return {"detail": OK}

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_USER_ID_PROVIDED
        )
    
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=SERVER_ERROR_SOMETHING_WITH_THE_DATA
        )
