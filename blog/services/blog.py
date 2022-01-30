from ..schemas.blog import BlogPostCreate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.blog import BlogPostItem
from ..utils.service_result import ServiceResult
from datetime import datetime
from typing import Union

'''
Notice how the error handling is simple.
If we can confirm what we're looking for isn't there,
we return a ServiceResult fed with the Exception object.

Otherwise we return a ServiceResult with the actual item
we found.
'''
class BlogService(AppService):
    def create_item(self, item: BlogPostCreate) -> ServiceResult:
        # Insert blog post
        blogpost_item = BlogCRUD(self.db).create_item(item)
        # Afterwards try to retreive it.
        if not blogpost_item:
            # If it isn't there, return an exception.
            return ServiceResult(AppException.BlogGetPost())
        return ServiceResult(blogpost_item)

        # Get post by providing the post's title.
    def get_item(self, blogpost_title: str):
        post_item = BlogCRUD(self.db).get_item(blogpost_title)
        if not post_item:
            return ServiceResult(AppException.BlogCreateItem({"blogpost_title": post_item}))

        return ServiceResult(post_item)

class BlogCRUD(AppCRUD):
    def create_item(self, item: BlogPostCreate) -> BlogPostItem:
        post_item = BlogPostItem(date_time=datetime.now(),
                                 title=item.title,
                                 body=item.body)
        self.db.add(post_item)
        self.db.commit()
        self.db.refresh(post_item)
        return post_item

    def get_item(self, item_title: str) -> Union[BlogPostItem, None]:
        post_item = self.db.query(BlogPostItem).filter(BlogPostItem.title == item_title).first()
        if post_item:
            return post_item
        return None
