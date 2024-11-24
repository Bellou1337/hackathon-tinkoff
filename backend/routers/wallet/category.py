from fastapi import Body, APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select, insert, delete
from ...database import get_async_session
from ...models import user, category, wallet, transaction 
from ...schemas import NewCategory, ResponseDetail, ReadCategory, UpdateCategory, UserRead
from ...dependencies import current_user, current_superuser
from typing import Dict, List
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
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_ALREADY_EXISTS}
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
async def set_new_category(
        category_data: NewCategory, 
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_superuser)
    ):
    
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



@category_router.post(
    "/delete",
    responses={
        200: {"model": ResponseDetail,"detail": OK},
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
async def remove_category(
        category_id: int = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_superuser)
    ): 

    query = delete(category).where(category.c.id == category_id)
    
    await session.execute(query)
    await session.commit()
    
    return {"detail" : OK}


@category_router.post(
    "/get",
    responses={
        200: {"model": ReadCategory},
        404: {
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_NOT_FOUND}
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
    "/get_list",
    responses={
        200: {"model": list[ReadCategory]},
        404: {
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_NOT_FOUND}
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
async def get_category_list(
        category_ids: list[int] = Body(embed=True),
        session: AsyncSession = Depends(get_async_session)
    ):
    
    stmt = select(category).where(category.c.id.in_(category_ids))

    result = (await session.execute(stmt)).all()
    
    if not result:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_NOT_FOUND,   
        )

    res: list[ReadCategory] = []

    for item in result:
        res.append(ReadCategory(id=item[0], name=item[1], is_income=item[2]))

    return res


@category_router.post(
    "/update",
    responses={
        200: {"model": ResponseDetail, "detail": OK},
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
async def update_category(
        category_data: UpdateCategory = Body(embed=True),
        session: AsyncSession = Depends(get_async_session),
        user: UserRead = Depends(current_superuser)
    ):

    
    stmt = update(category).where(category.c.id == category_data.id)

    if category_data.name is not None:
        stmt = stmt.values(name=category_data.name)

    if category_data.is_income is not None:
        stmt = stmt.values(is_income=category_data.is_income)
    
    await session.execute(stmt)
    await session.commit()

    return {"detail": OK}



@category_router.get(
    "/get_all",
    responses={
        200: {"model": List[ReadCategory]},
        404: {
            "content": {
                "application/json": {
                    "example": {"detail": CATEGORY_NOT_FOUND}
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
async def get_all_category(
        session: AsyncSession = Depends(get_async_session)
    ):

    stmt = select(category.c.name, category.c.is_income, category.c.id)
    
    result = await session.execute(stmt)
    rows = result.all()
    
    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CATEGORY_NOT_FOUND
        )
    
    return [
        ReadCategory(
            name = row[0],
            is_income = row[1],
            id = row[2]
        ) for row in rows
    ]
