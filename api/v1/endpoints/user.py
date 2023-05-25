from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session
from models.generic_model import User

router = APIRouter()

@router.get("/users/{user_id}", response_model=)
async def get_persons(db: AsyncSession = Depends(get_session)):
    query = User.__table__.select().where(User.id == user_id)
    return await database.fetch_one(query)


@router.post("/users")
async def post_user(user: UserModel):
    new_user = User.__table__.insert().values(
        name=user.name,
        email=user.email,
        password=user.password,
        role_id=user.role_id,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
