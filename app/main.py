from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Py Market Crawl")

app.include_router(router)