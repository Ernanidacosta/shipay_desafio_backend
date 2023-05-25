from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from core.configs import settings
from sqlmodel import Field, SQLModel


class RoleModel(SQLModel, table=True):
    __tablename__: str = "roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    description: str


class ClaimModel(SQLModel, table=True):
    __tablename__: str = "claims"

    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    active: bool

class UserModel(SQLModel, table=True):
    __tablename__: str = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship("RoleModel", backref="users")



class UserClaimModel(settings.DBBaseModel):
    __tablename__ = "user_claims"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), primary_key=True)

    user = relationship("UserModel", backref="claims")
    claim = relationship("ClaimModel", backref="users")
