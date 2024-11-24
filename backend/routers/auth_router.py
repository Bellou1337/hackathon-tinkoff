from ..auth.auth import SECRET
from ..auth import auth_backend, fastapi_users
from ..schemas import UserCreate, UserRead, UserUpdate, ResponseDetail
from ..dependencies import current_user
from ..database import get_async_session
from ..models import user
from ..auth.manager import smtp_sender
from ..general_data import templates
from ..details import *

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select
from fastapi import APIRouter, HTTPException, APIRouter, Depends, status, Body, Request
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from typing import Optional

router = APIRouter()

ALGORITHM = "HS256"

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/jwt"
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)

def create_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

@router.post(
    "/change_email/get_token",
    responses= {
        200: {
            "content": {
                "application/json": {
                    "example": {"detail": OK}
                }
            }
        },
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": "ERROR NAME"}
                }
            }
        },
    }
)
async def set_new_email(request : Request, new_email: str = Body(embed=True, examples=["user@example.com"]), user_info = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    if len(new_email) < 6 or len(new_email) > 255:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=EMAIL_LENGTH_IS_INVALID
        )
    
    stmt = select(user.c.email).where(user.c.email == new_email)
    data = (await session.execute(stmt)).first()

    if data is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=THIS_EMAIL_IS_ALREADY_IN_USE
        )

    token = create_token(
        {
            "sub": user_info.id,
            "email": new_email,
            "email_verified": user_info.email
        },
        timedelta(days=1)
    )

    html = templates.TemplateResponse(
        request=request, name="email/change_email.html", context={
            "username": user_info.username,
            "token": token
            }
    )

    smtp_sender.send_HTML_mail_task(new_email, "Смена почты", html.body.decode())

    return {"detail": OK}
    


@router.post(
    "/change_email/use_token",
    responses= {
        200: {
            "content": {
                "application/json": {
                    "example": {"detail": OK}
                }
            }
        },
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": "ERROR NAME"}
                }
            }
        },
        404: {
            "content": {
                "application/json": {
                    "example": {"detail": USER_NOT_FOUND}
                }
            }
        },
    }
)
async def set_new_email(token: str = Body(embed=True), session: AsyncSession = Depends(get_async_session)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])

        user_id: str = payload.get("sub")
        new_email: str = payload.get("email")
        now_email: str = payload.get("email_verified")

        if user_id is None or new_email is None or now_email is None:
            raise InvalidTokenError()
        
        stmt = select(user).where(user.c.id == user_id)
        user_ = (await session.execute(stmt)).fetchone()

        if user_ == None or now_email != user_[1]:
            raise InvalidTokenError()

        stmt = update(user).where(user.c.id == user_id).values(email=new_email)
        await session.execute(stmt)
        await session.commit()

        return {"detail": OK}
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_TOKEN
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=EMAIL_LENGTH_IS_INVALID
        )
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=USER_NOT_FOUND
        )