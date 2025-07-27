from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Feed(Base):
    __tablename__ = "feed_action"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    action = Column(String)
    time = Column(DateTime)

    user = relationship("User")
    post = relationship("Post")

