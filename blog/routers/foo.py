from fastapi import APIRouter, Depends

from services.foo import FooService
from schemas.foo import FooItem, FooItemCreate

from utils.service_result import handle_result
from config.database import get_db

'''
Routers and their routes are
defined in modules within the routers package. Each
route instantiates the respective service and passes on the database
session from the request dependency. Handled by handle_result(), the
service result (either the requested data as the result of a successful
operation or an exception) is returned. In case of an exception, instead of
(and before) returning any response, the app exception handler in main picks
up handling the exception and returns a response.
'''

router = APIRouter(
    prefix="/foo",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/item/", response_model=FooItem)
async def create_item(item: FooItemCreate, db: get_db = Depends())
    result = FooService(db).create_item(item)
    return handle_result(result)

@router.get("/item/{item_id}", response_model=FooItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).get_item(item_id)
    return handle_result(result)
