from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session, redis_db
from ..schemas import GetTransaction, GeminiResponse
from ..details import *
from .wallet.transaction import transaction_by_date  
from .wallet.category import get_category_list
from ..mycelery import prompt_sender

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
async def gemini(gemini_data: GetTransaction, session: AsyncSession = Depends(get_async_session)):
    
    try:
        
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
               
        redis_data = redis_db.get(key)
        
        if redis_data is not None:
            redis_data.decode('utf-8')        
            return redis_data
            
        redis_db.set(key, -1, 172_800)
        prompt_sender(prompt_message, key)
        
    
    except HTTPException:
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = NO_TRANSACTIONS_FOUND
            )
    
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = API_ERROR_SOMETHING_WITH_THE_DATA
        )
