from pydantic import BaseModel
from datetime import datetime

class BlogBase(BaseModel):
    body: str

class BlogPostCreate(BlogBase):
    title: str

class BlogPostItem(BlogBase):
    date_time: datetime

    class Config:
        orm_mode = True
