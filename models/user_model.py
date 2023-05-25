from datetime import date as date_type
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from core.configs import settings


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    created_at: date_type = Column(Date, nullable=False)
    updated_at: date_type = Column(Date)

    role = relationship("Role", backref="users")
