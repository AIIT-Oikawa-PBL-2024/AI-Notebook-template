from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserCreateResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True


class User(UserBase):
    id: int

    class Config:
        from_attributes = True