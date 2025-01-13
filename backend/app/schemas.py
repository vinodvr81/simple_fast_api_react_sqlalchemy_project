from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True