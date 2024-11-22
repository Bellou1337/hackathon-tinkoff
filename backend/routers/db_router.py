from fastapi import HTTPException, APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select
from ..database import get_async_session
from ..models import user
from ..schemas import ChangeEmail
from ..schemas import ChangeEmailData
from ..dependencies import current_user
from typing import Dict

router = APIRouter()


@router.post("/change_email", response_model=ChangeEmailData)
async def set_new_email(user_data: ChangeEmail, user_info=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    try:

        if len(user_data.new_email) < 6 or len(user_data.new_email) > 255:
            return {"detail": "Email length is invalid"}

        stmt = update(user).where(user.c.id == user_info.id).values(
            email=user_data.new_email)
        await session.execute(stmt)
        await session.commit()

        return {"detail": "Email update"}
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "Email length is invalid"}
        )
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"detail": "User not found"}
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"detail": "server error something with the data"}
        )