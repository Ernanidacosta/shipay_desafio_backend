from datetime import date
from typing import Optional
from pydantic import BaseModel as SCBaseModel


class Role(SCBaseModel):
    id: Optional[int]
    description: str

    class Config:
        orm_mode = True


class Claim(SCBaseModel):
    id: Optional[int]
    description: str
    active: bool

    class Config:
        orm_mode = True


class User(SCBaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    role_id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class UserClaimBase(SCBaseModel):
    user_id: int
    claim_id: int
