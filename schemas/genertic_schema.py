from datetime import date
from typing import Optional
from pydantic import BaseModel


class Role(RoleBase):
    id: Optional[int]
    description: str

    class Config:
        orm_mode = True

class Claim(ClaimBase):
    id: Optional[int]
    description: str
    active: bool

    class Config:
        orm_mode = True


class User(UserBase):
    id: Optional[int]
    name: str
    email: str
    password: str
    role_id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class UserClaimBase(BaseModel):
    user_id: int
    claim_id: int
