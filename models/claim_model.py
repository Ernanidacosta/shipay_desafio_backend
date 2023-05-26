from typing import Optional
from sqlmodel import SQLModel, Field


class ClaimModel(SQLModel, table=True):
    __tablename__: str = "claims"

    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    active: bool
