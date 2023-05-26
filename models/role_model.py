from typing import Optional
from sqlmodel import Field, SQLModel


class RoleModel(SQLModel, table=True):
    __tablename__: str = "roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
