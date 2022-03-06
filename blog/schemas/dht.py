from pydantic import BaseModel
from datetime import datetime

class DHTItemBase(BaseModel):
    time_log: str

# This is the schema that the endpoint
# expects to receive from POST
class DHTItemCreate(DHTItemBase):
    read_time: datetime
    humidity: float
    temperature: float

class DHTItem(DHTItemBase):
    humidity: float
    temperature: float

    class Config:
        orm_mode = True
