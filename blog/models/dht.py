'''
SQLAlchemy models are defined in the models package. They define how data is
stored within the relational database. They are referenced from AppCRUD. If needed, make sure
to differentiate between FooItem models (SQLAlchemy) and FooItem schemas (Pydantic) by
appropriate import namespacing
'''
from sqlalchemy import Float, Column, DateTime
from ..config.database import Base

class DHTItem(Base):
    __tablename__ = "dht_data"

    read_time = Column(DateTime, primary_key=True, index=True)
    humidity = Column(Float(32))
    public = Column(Float(32))
