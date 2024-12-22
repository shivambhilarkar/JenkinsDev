from fastapi import FastAPI
from app.routers import items

app = FastAPI(title="Sample API", description="A sample FastAPI application")

app.include_router(items.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Sample API"} 