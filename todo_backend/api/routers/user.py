from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
from api.schemas.user import UserCreate, UserResponse
from api.cruds import user as user_crud

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await user_crud.get_user_by_email(db, user_create.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = await user_crud.create_user(db, user_create)
    return user
