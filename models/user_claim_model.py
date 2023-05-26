from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from models.user_model import UserModel
from models.claim_model import ClaimModel


class UserClaimModel(SQLModel, table=True):
    __tablename__ = "user_claims"
    
    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="users.id")
    claim_id: int = Field(default=None, foreign_key="claims.id")

    user: UserModel = Relationship(back_populates="claims")
    claim: ClaimModel = Relationship(back_populates="users")
