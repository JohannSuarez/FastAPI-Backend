from sqlalchemy import Integer, String, Boolean, Column, DateTime
from ..config.database import Base

class BlogPostItem(Base):
    __tablename__ = "blog"

    date_time = Column(DateTime, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
