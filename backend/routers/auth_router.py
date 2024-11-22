from ..auth.auth import SECRET
from ..auth import auth_backend, fastapi_users
from ..schemas import UserCreate, UserRead, UserUpdate, ChangeEmailData, ChangeEmail
from ..dependencies import current_user
from ..database import get_async_session
from ..models import user
from ..auth.manager import smtp_sender
from ..general_data import templates

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, select
from fastapi import APIRouter, HTTPException, APIRouter, Depends, status, Body, Request, Query
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone

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

@router.post("/change_email/get_token")
async def set_new_email(email_data: ChangeEmail, user_info = Depends(current_user), request = Request):
    if len(email_data.new_email) < 6 or len(email_data.new_email) > 255:
        return {"detail": "Email length is invalid"}
    
    token = create_token(
        {
            "sub": user_info.id,
            "email": email_data.new_email,
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

    smtp_sender.send_HTML_mail(email_data.new_email, "Смена почты", html.body.decode())

    return {"detail": "OK"}
    


@router.post("/change_email/use_token", response_model=ChangeEmailData)
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

        return {"detail": "Email update"}
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Token"
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email length is invalid"
        )
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error something with the data"
        )