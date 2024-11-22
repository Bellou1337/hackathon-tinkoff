from fastapi import FastAPI, Depends

from .routers import wallet

from .routers import auth_router


app = FastAPI(
    title = "Hackathon API",    
)

app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    wallet.router,
    prefix="/wallet",
    tags=["wallet"]
)

@app.get('/')
async def root():
    return {'message': 'Hello World'}