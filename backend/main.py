from fastapi import FastAPI, Depends

from .routers import auth_router, db_router


app = FastAPI(
    title = "Hackathon API",    
)

app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    db_router.router,
    prefix="/db",
    tags=["database"]
)

@app.get('/')
async def root():
    return {'message': 'Hello World'}