from pydantic import BaseModel

class PostGet(BaseModel):
    id: int
    text: str
    topic: str
    author_id: int

    class Config:
        orm_mode = True

