from sqlalchemy import Column, Integer, String, Date
from core.configs import settings


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship("Role", backref="users")
