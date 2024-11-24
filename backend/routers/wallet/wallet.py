from fastapi import Body, APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, wallet, transaction, category
from ...schemas import NewWallet, ResponseDetail, RemoveWallet,UpdateWallet, UserWalletId, ReadWallet, WhalletId, UserRead, NewWalletByUserId, GetTransaction, ReadTransaction
from ...dependencies import current_user
from typing import List
from ...details import *
from ...dependencies import current_user, current_superuser

from fpdf import FPDF

wallet_router = APIRouter(
    prefix = "/wallet",
    tags = ["wallet"]
)

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

async def check_ownership_wallet(wallet_id: int, user_id, session: AsyncSession) -> bool:
    stmt = select(wallet.c.user_id).where(wallet.c.id == wallet_id)
    data = await session.execute(stmt)
    
    row = data.first()
    
    if not row:
        return False

    return user_id == row[0]

async def check_can_read_wallet(wallet_id: int, user_id, session: AsyncSession) -> bool:
    stmt = select(wallet.c.user_id, wallet.c.is_shared).where(wallet.c.id == wallet_id)
    data = await session.execute(stmt)
    
    row = data.first()
    
    if not row:
        return False

    return user_id == row[0] or row[1]

@wallet_router.post(
    "/add",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully created wallet"},
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_OR_TRANSACTION_NOT_FOUND}
                }
            }
        },
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        500: {
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
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):
    
    query = insert(wallet).values(
        name = wallet_data.name,
        user_id = user.id
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
    "/add_by_user_id",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully created wallet"},
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_OR_TRANSACTION_NOT_FOUND}
                }
            }
        },
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
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
async def add_new_wallet_by_user_id(
        wallet_data: NewWalletByUserId, 
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_user)
    ):

    if not user.is_superuser and wallet_data.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)
    
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
    "/remove",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully removed wallet"},
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {
            "content": {
                "application/json": {
                    "example": {"detail": WALLET_NOT_FOUND}
                }
            }
        },
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def remove_wallet(wallet_data: RemoveWallet,session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):
    
    stmt = select(wallet).where(wallet.c.id == wallet_data.id)
    result = await session.execute(stmt)
    
    data = result.first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=WALLET_NOT_FOUND
        )
    
    if not user.is_superuser and data[1] != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    query = delete(wallet).where(wallet.c.id == wallet_data.id)
    await session.execute(query)
    await session.commit()

    return {"detail": OK}

@wallet_router.post(
    "/update",
    responses={
        200: {"model": ResponseDetail, "description": "Successfully updated wallet"},
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": INVALID_USER_ID_PROVIDED}
                }
            }
        },
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def update_wallet(wallet_data: UpdateWallet,session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):

    try:
        stmt = select(wallet).where(wallet.c.id == wallet_data.id)
        result = await session.execute(stmt)
    
        data = result.first()

        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=WALLET_NOT_FOUND)
        
        if not user.is_superuser and data[1] != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

        update_values = {}
        if wallet_data.name is not None:
            update_values["name"] = wallet_data.name
        if wallet_data.balance is not None:
            update_values["balance"] = wallet_data.balance
        if wallet_data.user_id is not None:
            update_values["user_id"] = wallet_data.user_id
        if wallet_data.is_shared is not None:
            update_values["is_shared"] = wallet_data.is_shared
        
        query = update(wallet).where(wallet.c.id == wallet_data.id).values(**update_values)
        await session.execute(query)
        await session.commit()
        
        return {"detail": OK}

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_USER_ID_PROVIDED
        )

@wallet_router.post(
    "/get_by_user_id",
    responses={
        200: {"model": List[ReadWallet], "description": "Successfully retrieved wallet"},
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def get_wallet_by_user_id(wallet_data: UserWalletId, session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):

    if not user.is_superuser and wallet_data.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    stmt = select(wallet).where(wallet.c.user_id == wallet_data.user_id)
    result = await session.execute(stmt)

    rows = result.all()
    
    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=WALLET_NOT_FOUND
        )

    res = [
        ReadWallet(
            id=row[0],
            name=row[2],
            balance=row[3],
            user_id=row[1]
        ) for row in rows
    ]

    return res

@wallet_router.get(
    "/get_my",
    responses={
        200: {"model": List[ReadWallet], "description": "Successfully retrieved wallet"},
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def get_wallet_my(user: UserRead = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    stmt = select(wallet).where(wallet.c.user_id == user.id)
    result = await session.execute(stmt)

    rows = result.all()
    
    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=WALLET_NOT_FOUND
        )

    return [
        ReadWallet(
            id=row[0],
            name=row[2],
            balance=row[3],
            user_id=row[1]
        ) for row in rows
    ]

@wallet_router.post(
    "/get_by_id",
    responses={
        200: {"model": ReadWallet, "description": "Successfully retrieved wallet"},
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def get_wallet_by_id(wallet_data: WhalletId, session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):
       
    stmt = select(wallet).where(wallet.c.id == wallet_data.id)
    data = await session.execute(stmt)
    
    row = data.first()
    
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=WALLET_NOT_FOUND)
    
    res = ReadWallet(
        id=row[0],
        name=row[2],
        balance=row[3],
        user_id=row[1]
    )

    if user.is_superuser or (await check_can_read_wallet(wallet_data.id, user.id, session)):
        return res
    
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

@wallet_router.post(
    "/pdf_generate",
    responses={
        200: {"model": ReadWallet, "description": "Successfully retrieved wallet"},
        403: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_PERMISSION_ERROR}
                }
            }
        },
        404: {"description": "Not Found", "content": {"application/json": {"example": {"detail": WALLET_NOT_FOUND}}}},
        500: {"description": "Internal Server Error", "content": {"application/json": {"example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}}}}
    }
)
async def get_wallet_pdf(wallet_data: GetTransaction, session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):
       
    if not (user.is_superuser or (await check_can_read_wallet(wallet_data.wallet_id, user.id, session))):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)
    
    data = await transaction_by_date(wallet_data, session)

    category_ids = []
    for i in data:
        if i.category_id not in category_ids:
            category_ids.append(i.category_id)

    stmt = select(category.c.id, category.c.name).where(category.c.id.in_(category_ids))
    category_datas = (await session.execute(stmt)).all()

    categories = {}
    for i in category_datas:
        categories[i[0]] = i[1]

    head = ("Название", "Категория", "Сумма", "Дата")

    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("DejaVu", '', 'DejaVuSans.ttf')
    pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf")

    pdf.set_font("DejaVu", size=12)

    stmt = select(wallet.c.name).where(wallet.c.id == wallet_data.wallet_id)
    wallet_name = (await session.execute(stmt)).first()

    pdf.write(text=wallet_name[0])
    pdf.ln()
    pdf.ln()

    with pdf.table(cell_fill_color=200, cell_fill_mode="ROWS") as table:
        row = table.row()
        for datum in head:
            row.cell(datum)
            
        for data_row in data:
            row = table.row()

            row.cell(str(data_row.title))
            row.cell(str(categories[data_row.category_id]))
            row.cell(str(data_row.amount))
            row.cell(str(data_row.date.strftime("%d.%m.%Y %H:%M")))


    filename = "table.pdf"
    headers = {
        "Content-Disposition": f"attachment; filename={filename}"
    }

    return Response(content=bytes(pdf.output()), media_type="application/pdf", headers=headers)
