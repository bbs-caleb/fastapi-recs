from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    gender: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str

    class Config:
        orm_mode = True

