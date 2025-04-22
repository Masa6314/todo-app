from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from api.models.user import User
from api.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user_create: UserCreate):
    hashed_password = pwd_context.hash(user_create.password)
    user = User(email=user_create.email, hashed_password=hashed_password, user_name=user_create.user_name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
