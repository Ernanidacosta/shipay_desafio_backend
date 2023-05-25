from datetime import date as date_type
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from databases import Database
from core.configs import settings



class RoleModel(settings.DBBaseModel):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)


class ClaimModel(settings.DBBaseModel):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)


class UserModel(settings.DBBaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship("Role", backref="users")


class UserClaimModel(settings.DBBaseModel):
    __tablename__ = "user_claims"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), primary_key=True)

    user = relationship("User", backref="claims")
    claim = relationship("Claim", backref="users")
