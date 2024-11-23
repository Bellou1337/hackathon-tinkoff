from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import wallet

from .routers import auth_router


app = FastAPI(
    title = "Hackathon API",    
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://git-ts2.ru:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    wallet.router
)

@app.get('/')
async def root():
    return {'message': 'Hello World'}