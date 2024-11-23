from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import transaction, category, wallet
from ...schemas import NewTransaction, ResponseDetail, UpdateTransaction, GetTransaction, ReadTransaction, UserRead
from ...dependencies import current_user
from typing import Dict
from ...details import *
from .wallet import check_ownership_wallet, check_can_read_wallet
from ...dependencies import current_user, current_superuser

transaction_router = APIRouter(
    prefix = "/transaction",
    tags = ["transaction"]
)
                
@transaction_router.post(
    "/add",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully created transaction"},
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
async def add_new_transaction(
        transaction_data: NewTransaction, 
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):
    try:

        if not (await check_ownership_wallet(transaction_data.wallet_id, user.id, session)) and not user.is_superuser:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

        query = insert(transaction).values(
            title = transaction_data.title,
            amount = transaction_data.amount,
            date = transaction_data.date.replace(tzinfo=None),
            category_id = transaction_data.category_id,
            wallet_id = transaction_data.wallet_id
        )
        await session.execute(query)

        query = select(category).where(category.c.id == transaction_data.category_id)
        category_data = (await session.execute(query)).fetchone()

        amount = transaction_data.amount
        if not category_data[2]:
            amount = -amount
        
        query = (
            update(wallet)
            .where(wallet.c.id == transaction_data.wallet_id)
            .values(balance=wallet.c.balance + amount)
        )
        await session.execute(query)

        await session.commit()

        return {"detail": OK}

    except IntegrityError:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_OR_TRANSACTION_NOT_FOUND,   
        )



@transaction_router.post(
    "/delete",
    responses={
        200: {"model": ResponseDetail,"detail": OK},
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"detail": TRANSACTION_NOT_FOUND}
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
async def remove_transaction(
        transaction_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ): 
    
    query = select(transaction).where(transaction.c.id == transaction_id)
    transaction_data = (await session.execute(query)).fetchone()

    if transaction_data is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = TRANSACTION_NOT_FOUND
        )
    
    if not (await check_ownership_wallet(transaction_data[1], user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    query = select(category).where(category.c.id == transaction_data[2])
    category_data = (await session.execute(query)).fetchone()

    if category_data is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = CATEGORY_NOT_FOUND
        )

    query = delete(transaction).where(transaction.c.id == transaction_id)
    await session.execute(query)


    amount = transaction_data[4]
    if category_data[2]:
        amount = -amount
    
    query = (
        update(wallet)
        .where(wallet.c.id == transaction_data[1])
        .values(balance=wallet.c.balance + amount)
    )
    await session.execute(query)
    await session.commit()
    
    return {"detail" : OK}

@transaction_router.post(
    "/get_by_date",
    responses={
        200: {"model": list[ReadTransaction]},
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
async def get_transaction_by_date(
        get_transaction_data: GetTransaction,
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):

    if not (await check_can_read_wallet(get_transaction_data.wallet_id, user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    res = await transaction_by_date(get_transaction_data, session)
    return res
    

async def transaction_by_date(
    get_transaction_data: GetTransaction,
    session: AsyncSession = Depends(get_async_session)
):        
    stmt = select(transaction).where(transaction.c.wallet_id == get_transaction_data.wallet_id, transaction.c.date.between(get_transaction_data.start.replace(tzinfo=None), get_transaction_data.end.replace(tzinfo=None)))
    
    data = (await session.execute(stmt)).all()
    res: list[ReadTransaction] = []
    
    for item in data:
        res.append(ReadTransaction(
            id=item[0],
            title=item[3],
            category_id=item[2],
            wallet_id=item[1],
            amount=item[4],
            date=item[5]
        ))

    return res


@transaction_router.post(
    "/get_by_id",
    responses={
        200: {"model": ReadTransaction},
        404: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"detail": TRANSACTION_NOT_FOUND}
                }
            }
        }
    }
)
async def get_transaction_by_id(
        transaction_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):
    
    stmt = select(transaction).where(transaction.c.id == transaction_id)
    
    item = (await session.execute(stmt)).fetchone()

    if item is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = TRANSACTION_NOT_FOUND
        )
    
    if not (await check_can_read_wallet(item[1], user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)
    
    return ReadTransaction(
            id=item[0],
            title=item[3],
            category_id=item[2],
            wallet_id=item[1],
            amount=item[4],
            date=item[5]
        )

@transaction_router.post(
    "/get_by_wallet_id",
    responses={
        200: {"model": list[ReadTransaction]}
    }
)
async def get_transaction_by_wallet_id(
        wallet_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):

    if not (await check_can_read_wallet(wallet_id, user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)
    
    stmt = select(transaction).where(transaction.c.wallet_id == wallet_id)
    
    data = (await session.execute(stmt)).all()
    
    res: list[ReadTransaction] = []
        
    for item in data:
        res.append(ReadTransaction(
            id=item[0],
            title=item[3],
            category_id=item[2],
            wallet_id=item[1],
            amount=item[4],
            date=item[5]
        ))

    return res

@transaction_router.post(
    "/update"
)
async def update_transaction(
        trasaction_data: UpdateTransaction = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):
    
    stmt = select(transaction.c.amount, transaction.c.category_id, transaction.c.wallet_id).where(transaction.c.id == trasaction_data.id)
    old_transaction_data = (await session.execute(stmt)).fetchone()

    if old_transaction_data is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = TRANSACTION_NOT_FOUND
        )

    old_amount, old_category_id, wallet_id = old_transaction_data

    if not (await check_ownership_wallet(wallet_id, user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    stmt = update(transaction).where(transaction.c.id == trasaction_data.id)

    query = select(category.c.is_income).where(category.c.id == old_category_id)
    old_category_is_income = (await session.execute(query)).fetchone()

    if old_category_is_income is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = CATEGORY_NOT_FOUND
        )

    old_category_is_income = old_category_is_income[0]
    new_category_is_income = old_category_is_income

    if trasaction_data.category_id is not None:
        query = select(category.c.is_income).where(category.c.id == trasaction_data.category_id)
        new_category_is_income = (await session.execute(query)).fetchone()

        if new_category_is_income is None:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = CATEGORY_NOT_FOUND
            )

        new_category_is_income = new_category_is_income[0]

    if trasaction_data.title is not None:
        stmt = stmt.values(title=trasaction_data.title)
    
    if trasaction_data.date is not None:
        stmt = stmt.values(date=trasaction_data.date.replace(tzinfo=None))
    
    if old_category_is_income != new_category_is_income and trasaction_data.amount is not None:
        new_amount = abs(trasaction_data.amount) + abs(old_amount)

        if not new_category_is_income:
            new_amount = -new_amount

        query = (
            update(wallet)
            .where(wallet.c.id == wallet_id)
            .values(balance=wallet.c.balance + new_amount)
        )
        
        await session.execute(query)

        stmt = stmt.values(category_id=trasaction_data.category_id)
        stmt = stmt.values(amount=trasaction_data.amount)

    elif old_category_is_income != new_category_is_income:
        if not old_category_is_income:
            old_amount = -old_amount

        query = (
            update(wallet)
            .where(wallet.c.id == wallet_id)
            .values(balance=wallet.c.balance - old_amount * 2)
        )
        await session.execute(query)

        stmt = stmt.values(category_id=trasaction_data.category_id)
        
    elif trasaction_data.amount is not None:
        new_amount = abs(trasaction_data.amount) - abs(old_amount)
        if not new_category_is_income:
            new_amount = -new_amount

        query = (
            update(wallet)
            .where(wallet.c.id == wallet_id)
            .values(balance=wallet.c.balance + new_amount)
        )
        
        await session.execute(query)
        stmt = stmt.values(amount=trasaction_data.amount)

    
    await session.execute(stmt)
    await session.commit()

    return {"detail" : OK}