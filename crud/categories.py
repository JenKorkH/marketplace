from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Category
from schemas import CategoryRead, CategoryCreate

async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def create_category(db: AsyncSession, category: CategoryCreate):
    new_category=Category(**category.model_dump())
    db.add(new_category)
    await db.commit()
    return new_category

