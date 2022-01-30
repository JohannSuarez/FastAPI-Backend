from fastapi import APIRouter, Depends
from ..services.blog import BlogService
from ..schemas.blog import BlogPostItem, BlogPostCreate

from ..utils.service_result import handle_result
from ..config.database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["items"],
    responses={404: {"description": "Not Found"}},
)

@router.post('/blog/', response_model=BlogPostItem)
async def create_post(item: BlogPostCreate, db: get_db = Depends()):
    result = BlogService(db).create_item(item)
    return handle_result(result)

@router.get("/blog/{title}", response_model=BlogPostItem)
async def get_post(title: str, db: get_db =Depends()):
    result = BlogService(db).get_item(title)
    return handle_result(result)
