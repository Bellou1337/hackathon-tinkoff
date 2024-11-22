from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, category, wallet, transaction 
from ...schemas import NewCategory, ResponseDetail, ReadCategory, UpdateCategory
from ...dependencies import current_user
from typing import Dict
from ...details import *

category_router = APIRouter(
    prefix = "/category",
    tags = ["category"]
)
                
@category_router.post(
    "/add",
    responses={
        200: {"model": NewCategory, "description": "Successfully created category"},
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_ALREADY_EXISTS}
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
async def set_new_category(
        category_data: NewCategory, 
        session: AsyncSession = Depends(get_async_session)
    ):
    
    try:
        stmt = select(category).where(category.c.name == category_data.name)
        
        result = await session.execute(stmt)
        
        if result.first():
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail=CATEGORY_ALREADY_EXISTS,
                
            )
        
        
        query = insert(category).values(
            name = category_data.name,
            is_income = category_data.is_income
        )
        
        await session.execute(query)
        await session.commit()
        
        return category_data
    
    except HTTPException:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = CATEGORY_ALREADY_EXISTS
        )
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = SERVER_ERROR_SOMETHING_WITH_THE_DATA
        )



@category_router.post(
    "/delete",
    responses={
        200: {"model": ResponseDetail,"detail": OK},
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
async def remove_category(
        category_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session)
    ): 
    
    try:        
        query = delete(category).where(category.c.id == category_id)
        
        await session.execute(query)
        await session.commit()
        
        return {"detail" : OK}
    
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = SERVER_ERROR_SOMETHING_WITH_THE_DATA
        )


@category_router.post(
    "/get",
    responses={
        200: {"model": ReadCategory},
        404: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_NOT_FOUND}
                }
            }
        }
    }
)
async def get_category(
        category_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session)
    ):
    
    stmt = select(category).where(category.c.id == category_id)
    
    result = (await session.execute(stmt)).first()
    
    if not result:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_NOT_FOUND,   
        )

    return ReadCategory(id=result[0], name=result[1], is_income=result[2])


@category_router.post(
    "/update"
)
async def update_category(
        category_data: UpdateCategory = Body(embed=True),
        session: AsyncSession = Depends(get_async_session)
    ):

    print(category_data)
    
    stmt = update(category).where(category.c.id == category_data.id)

    if category_data.name is not None:
        stmt = stmt.values(name=category_data.name)

    if category_data.is_income is not None:
        stmt = stmt.values(is_income=category_data.is_income)
    
    await session.execute(stmt)
    await session.commit()

    return {}