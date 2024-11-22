from fastapi import APIRouter

from .category import category_router

router = APIRouter()

router.include_router(category_router)

# TODO: category: edit, get