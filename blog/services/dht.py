from ..schemas.dht import DHTItemCreate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.dht import DHTItem
from ..utils.service_result import ServiceResult
from typing import Union
from datetime import datetime


class DHTCRUD(AppCRUD):

    def create_item(self, item: DHTItemCreate) -> DHTItem:
        dht_item = DHTItem(humidity=item.humidity,
                           temperature=item.temperature,
                           read_time=datetime.now())
        self.db.add(dht_item)
        self.db.commit()
        self.db.refresh(dht_item)

        return dht_item

    def get_item(self, date) -> Union[DHTItem, None]:
        dht_item = self.db.query(DHTItem).filter(DHTItem.read_time == date).first()

        if dht_item:
            return dht_item
        return None


class DHTService(AppService):
    def create_item(self, item: DHTItemCreate) -> ServiceResult:
        dht_item = DHTCRUD(self.db).get_item(item)
        if not dht_item:
            return ServiceResult(AppException.DHTCreateItem())
        return ServiceResult(dht_item)

    def get_item(self, date_time: str) -> ServiceResult:
        dht_item = DHTCRUD(self.db).get_item(date)

        if not dht_item:
            return ServiceResult(AppException.DHTGetItem({"date_time": read_time}))

        return ServiceResult(dht_item)
