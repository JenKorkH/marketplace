from fastapi import FastAPI
from routes.categories import router as category_router

app = FastAPI()

app.include_router(category_router)

