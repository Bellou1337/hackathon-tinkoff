from fastapi import HTTPException, APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ..database import get_async_session
from ..models import user, category, wallet, transaction 
from ..schemas import ChangeEmail, NewCategory, DeleteCategory, ResponseDetail
from ..schemas import ChangeEmailData
from ..dependencies import current_user
from typing import Dict
from ..details import *


router = APIRouter()
                
@router.post(
    "/add_category",
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
async def set_new_category(category_data: NewCategory, 
session: AsyncSession = Depends(get_async_session)):
    
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



@router.post(
    "/delete_category",
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
async def remove_category(category_data: DeleteCategory,
session: AsyncSession = Depends(get_async_session)): 
    
    try:
        stmt = select(category).where(category.c.id == category_data.id)
        
        result = await session.execute(stmt)
        
        if not result.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CATEGORY_NOT_FOUND)
        
        query = delete(category).where(category.c.id == category_data.id)
        
        await session.execute(query)
        await session.commit()
        
        return {"detail" : OK}
    
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = SERVER_ERROR_SOMETHING_WITH_THE_DATA
        )
                
    