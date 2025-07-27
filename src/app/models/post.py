from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    topic = Column(String)
    author_id = Column(Integer)  # есть в схеме курса

