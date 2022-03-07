'''
Routes belonging to service Foo are connected to methods
of FooService, which encapsulates all business logic of the service.
The return value are of type ServiceResult: Containing a value attribute
with returnable data or, in case of an exception, an AppException.

In both cases, the respective result is returned back "upwards" to the controller layer.
'''
from ..schemas.foo import FooItemCreate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.foo import FooItem
from ..utils.service_result import ServiceResult
from typing import Union

class FooService(AppService):
    def create_item(self, item: FooItemCreate) -> ServiceResult:
        foo_item = FooCRUD(self.db).create_item(item)
        if not foo_item:
            return ServiceResult(AppException.FooCreateItem())
        return ServiceResult(foo_item)

    def get_item(self, item_id: int) -> ServiceResult:
        foo_item = FooCRUD(self.db).get_item(item_id)
        if not foo_item:
            return ServiceResult(AppException.FooGetItem({"item_id": item_id}))

        if not foo_item.public:
            return ServiceResult(AppException.FooItemRequiresAuth())
        return ServiceResult(foo_item)

'''
CRUD helper methods perforrm operations on the database and are
subclassing AppCRUD. The database session is passed down from the
AppService instance. These methods are atomic and only concerned with
operation on the database. They do not contain any business logic.
'''
class FooCRUD(AppCRUD):
    def create_item(self, item: FooItemCreate) -> FooItem:
        foo_item = FooItem(description=item.description,
                           public=item.public)
        self.db.add(foo_item)
        self.db.commit()
        self.db.refresh(foo_item)
        return foo_item

    def get_item(self, item_id: int) -> Union[FooItem, None]:
        foo_item = self.db.query(FooItem).filter(FooItem.id == item_id).first()
        if foo_item:
            return foo_item
        return None
