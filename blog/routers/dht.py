from fastapi import APIRouter, Depends
from ..services.dht import DHTService
from ..schemas.dht import DHTItem, DHTItemCreate

from ..utils.service_result import handle_result
from ..config.database import get_db


router = APIRouter(
    prefix="/dht",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/dht/", response_model=DHTItem)
async def create_item(item: DHTItemCreate, db: get_db = Depends()):
    print(item)
    result = DHTService(db).create_item(item)
    return handle_result(result)

@router.get("/dht/{item_id}", response_model=DHTItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = DHTService(db).get_item(item_id)
    return handle_result(result)
