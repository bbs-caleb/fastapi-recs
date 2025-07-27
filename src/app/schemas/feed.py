from datetime import datetime
from pydantic import BaseModel
from app.schemas.user import UserGet
from app.schemas.post import PostGet

class FeedGet(BaseModel):
    id: int
    user_id: int
    post_id: int
    action: str
    time: datetime
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True

