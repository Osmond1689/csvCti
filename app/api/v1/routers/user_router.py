from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    return await user_service.create_user(user)

@router.get("/", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    return await user_service.get_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=User)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    return await user_service.get_user_by_id(user_id)

@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    return await user_service.update_user(user_id, user)

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    await user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}

@router.post("/{user_id}/change-password")
async def change_password(
    user_id: int,
    old_password: str,
    new_password: str,
    db: AsyncSession = Depends(get_db)
):
    user_service = UserService(db)
    await user_service.change_password(user_id, old_password, new_password)
    return {"message": "Password changed successfully"}
