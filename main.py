from datetime import datetime, date
from typing import Generator
import random
import string

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship, selectinload
from sqlalchemy.future import Engine, select
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


class Claim(Base):
    __tablename__ = 'claims'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    created_at = Column(Date, nullable=False, default=date.today)
    updated_at = Column(Date)
    role = relationship("Role", backref="users")


engine: Engine = create_async_engine('sqlite+aiosqlite:///database.db')
Session: sessionmaker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> Generator:
    async with Session() as session:
        yield session


async def create_tables() -> None:
    print('Creating database tables...')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print('Database tables created successfully')


create_tables()


app = FastAPI()


@app.post("/roles")
async def create_role(description: str, db: AsyncSession = Depends(get_session)):
    role = Role(description=description)
    db.add(role)
    await db.commit()
    return {"message": "Role created successfully"}


@app.get("/users/{role_id}/role")
async def get_user_role(role_id: int, db: AsyncSession = Depends(get_session)):
    user = await db.execute(select(User).options(selectinload(User.role)).filter(User.role_id == role_id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"role_description": user.role.description}


class UserCreate(BaseModel):
    name: str
    email: str
    role_id: int
    password: str = None


@app.post("/users")
async def create_user(user_create: UserCreate, db: AsyncSession = Depends(get_session)):
    password = user_create.password or generate_random_password()

    user = User(
        name=user_create.name,
        email=user_create.email,
        password=password,
        role_id=user_create.role_id,
        created_at=date.today()
    )

    db.add(user)
    await db.commit()

    return {"message": "User created successfully"}


def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
