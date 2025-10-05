from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import CategoryCreate, CategoryRead
from database import get_db
from crud.categories import *
router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[CategoryRead])
async def get_categories_route(db: AsyncSession=Depends(get_db)):
    categories = await get_categories(db)
    return categories

@router.post("/", response_model=CategoryCreate)
async def add_category_route(category: CategoryCreate, db:AsyncSession=Depends(get_db)):
    new_category = await create_category(db, category)
    return new_category