from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session, redis_db
from ..schemas import GetTransaction, GeminiResponse, GetGeminiRecomendation, UserRead
from ..details import *
from .wallet.transaction import transaction_by_date
from .wallet.category import get_category_list
from .wallet.wallet import check_ownership_wallet
from ..mycelery import prompt_sender
from ..dependencies import current_user, current_superuser

transaction_router = APIRouter(
    prefix = "/gemini",
    tags = ["gemini"]
)

@transaction_router.post(
    "/recomendations",
    responses={
        200: {
            "model": GeminiResponse,
            
            "description": "Successfully got recommendations"
        },
        404: {
            "description": "Not Found",
            "content": {
                "application/json": {
                    "example": {"detail": NO_TRANSACTIONS_FOUND}
                }
            }
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {"detail": API_ERROR_SOMETHING_WITH_THE_DATA}
                }
            }
        }
    }
)
async def gemini(gemini_data: GetTransaction, session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):
    
    if not (await check_ownership_wallet(gemini_data.wallet_id, user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    res = await transaction_by_date(gemini_data, session)
    
    if res is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = NO_TRANSACTIONS_FOUND
        )
    
    
    income = 0
    expenses = 0
    
    categories_dict = {}
    
    
    for data in res:
        categories_dict[data.title] = 0
        category_id = data.category_id
        all_categories = await get_category_list([category_id], session)
        money = data.amount      
        for category in all_categories:
            categories_dict[data.title]+= money
            if category.is_income == True:
                income+= money
            else:
                expenses+=money    
    
    prompt_message = f"Анализируй финансовые данные. Доходы: {income} руб., расходы {expenses} руб.:"
            
    for search in categories_dict:
        prompt_message+=f" {search}({categories_dict[search]})"
    
    prompt_message+=f"Дай рекомендации.Отвечай в таком формате: Советы которые вам помогут: 1. Совет.\n2. Совет\n...\nn. Совет. Пиши без лишних слов и форматирования текста.Каждый пункт должен начинаться с новой строки и быть пронумерованным.Пиши до 10 пунктов и всегда на русском языке."
    
    key = f"tinkoffhack.{gemini_data.wallet_id}"
                
    redis_db.set(key, -1, 172_800)
    prompt_sender.delay(prompt_message, key)
    # prompt_sender(prompt_message, key)


@transaction_router.post(
    "/get_recomendations",
    responses={
        200: {
            "model": GeminiResponse,
            
            "description": "Successfully got redis key"
        },
        404: {
            "description": "Not Found",
            "content": {
                "application/json": {
                    "example": {"detail": NO_KEY}
                }
            }
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {"detail": REDIS_ERROR_SOMETHING_WITH_THE_DATA}
                }
            }
        }
    }
)
async def get_recomendation(gemini_data: GetGeminiRecomendation, session: AsyncSession = Depends(get_async_session), user: UserRead = Depends(current_user)):

    if not (await check_ownership_wallet(gemini_data.wallet_id, user.id, session)) and not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=USER_PERMISSION_ERROR)

    key = f"tinkoffhack{gemini_data.wallet_id}"
    stmt = redis_db.get(key)
    
    if stmt is not None:
        return {"detail" : stmt.decode('utf-8')}
    
    
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = NO_KEY
        )        
