from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str 
    photo_url: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate

class CategoryRead(CategoryBase):
    id: int

    class Config:
        from_attributes = True