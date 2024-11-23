from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, wallet, transaction 
from ...schemas import NewTransaction, ResponseDetail
from ...dependencies import current_user
from typing import Dict
from ...details import *

transaction_router = APIRouter(
    prefix = "/transaction",
    tags = ["transaction"]
)
                
@transaction_router.post(
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
async def add_new_transaction(
        transaction_data: NewTransaction, 
        session: AsyncSession = Depends(get_async_session)
    ):
    
    query = insert(transaction).values(
        title = transaction_data.title,
        amount = transaction_data.amount,
        date = transaction_data.date.replace(tzinfo=None),
        category_id = transaction_data.category_id,
        wallet_id = transaction_data.wallet_id
    )

    try:
        await session.execute(query)
        await session.commit()

        return {"detail": OK}

    except IntegrityError:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_OR_TRANSACTION_NOT_FOUND,   
        )



# @category_router.post(
#     "/delete",
#     responses={
#         200: {"model": ResponseDetail,"detail": OK},
#         400: {
#             "description": "Bad Request",
#             "content": {
#                 "application/json": {
#                     "example": {"detail": CATEGORY_NOT_FOUND}
#                 }
#             }
#         },
#         500: {
#             "description": "Internal Server Error",
#             "content": {
#                 "application/json": {
#                     "example": {"detail": SERVER_ERROR_SOMETHING_WITH_THE_DATA}
#                 }
#             }
#         }
#     }
# )
# async def remove_category(
#         category_id: int = Body(embed=True),
#         session: AsyncSession = Depends(get_async_session)
#     ): 
    
#     try:        
#         query = delete(category).where(category.c.id == category_id)
        
#         await session.execute(query)
#         await session.commit()
        
#         return {"detail" : OK}
    
#     except Exception:
#         raise HTTPException(
#             status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail = SERVER_ERROR_SOMETHING_WITH_THE_DATA
#         )


# @category_router.post(
#     "/get",
#     responses={
#         200: {"model": ReadCategory},
#         404: {
#             "description": "Bad Request",
#             "content": {
#                 "application/json": {
#                     "example": {"detail": CATEGORY_NOT_FOUND}
#                 }
#             }
#         }
#     }
# )
# async def get_category(
#         category_id: int = Body(embed=True),
#         session: AsyncSession = Depends(get_async_session)
#     ):
    
#     stmt = select(category).where(category.c.id == category_id)
    
#     result = (await session.execute(stmt)).first()
    
#     if not result:
#         raise HTTPException(
#             status_code= status.HTTP_404_NOT_FOUND,
#             detail=CATEGORY_NOT_FOUND,   
#         )

#     return ReadCategory(id=result[0], name=result[1], is_income=result[2])


# @category_router.post(
#     "/update"
# )
# async def update_category(
#         category_data: UpdateCategory = Body(embed=True),
#         session: AsyncSession = Depends(get_async_session)
#     ):

#     print(category_data)
    
#     stmt = update(category).where(category.c.id == category_data.id)

#     if category_data.name is not None:
#         stmt = stmt.values(name=category_data.name)

#     if category_data.is_income is not None:
#         stmt = stmt.values(is_income=category_data.is_income)
    
#     await session.execute(stmt)
#     await session.commit()

#     return {}