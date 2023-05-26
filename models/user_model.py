from datetime import date, datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from models.role_model import RoleModel


class UserModel(SQLModel, table=True):
    __tablename__: str = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email = str
    password = str
    role_id: int = Field(default=None, foreign_key="roles.id")
    created_at: date = Field(default=datetime.date, nullable=False)
    updated_at: date = Field(default=datetime.date, nullable=True)

    role: RoleModel = Relationship(back_populates="users")
