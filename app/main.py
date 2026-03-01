from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    # Anything before the yield below will execture pre app startup
    yield

app = FastAPI(title="Py Market Crawl")
app.include_router(router)