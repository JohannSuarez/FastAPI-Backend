from sqlalchemy import Integer, String, Boolean, Column, DateTime
from ..config.database import Base

class BlogPostItem(Base):
    __tablename__ = "blog"

    read_time = Column(DateTime, primary_key=True, index=True)
    humidity = Column(Float)
    temperature = Column(Float)
