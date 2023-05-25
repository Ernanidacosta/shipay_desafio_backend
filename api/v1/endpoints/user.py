from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session
from models.generic_model import UserModel
from schemas.genertic_schema import User

router = APIRouter()

@router.get("/user/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).where(UserModel.id == user_id)
        return await session.execute(query)


@router.post("/user")
async def post_user(user: User, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=user.password,
        role_id=user.role_id,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    db.add(new_user)
    await db.commit()
    return new_user
