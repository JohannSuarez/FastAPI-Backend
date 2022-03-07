from pydantic import BaseModel
from datetime import datetime

class DHTItemBase(BaseModel):
    humidity: float
    temperature: float

# This is the schema that the endpoint
# expects to receive from POST
class DHTItemCreate(DHTItemBase):
    pass

class DHTItem(DHTItemBase):
    read_time: datetime

    class Config:
        orm_mode = True
