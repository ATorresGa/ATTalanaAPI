from pydantic import BaseModel
from typing import Optional

class UserCreateSchema (BaseModel):
    password:str
    email:str

class UserResponseSchema(BaseModel):
    id: int
    email:str

class UserEditSchema(BaseModel):
    email: str
    role: str
    triviaId: int

class UserEditResponseSchema(BaseModel):
    id: int
    email: str
    role: str
    triviaId: int

class Config:
    orm_mode=True