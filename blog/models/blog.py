from sqlalchemy import Integer, String, Boolean, Column, DateTime, Float
from ..config.database import Base

class BlogPostItem(Base):
    __tablename__ = "blog"

    date_time = Column(DateTime, primary_key=True, index=True)
    # The SQLAlchemy Docs isn't clear about the parameter provided to Float
    # Does it mean the Float size is 256 bits or 256 bytes?
    # I wouldn't want a 256 byte Float.
    title = Column(String)
    body = Column(String)
