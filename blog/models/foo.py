'''
SQLAlchemy models are defined in the models package. They define how data is
stored within the relational database. They are referenced from AppCRUD. If needed, make sure
to differentiate between FooItem models (SQLAlchemy) and FooItem schemas (Pydantic) by
appropriate import namespacing
'''
from sqlalchemy import Integer, String, Boolean, Column
from ..config.database import Base

class FooItem(Base):
    __tablename__ = "foo_items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    public = Column(Boolean, default=False)
