from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import user as user_crud
from app.schemas.user import UserCreate, UserUpdate, User
from app.core.security import verify_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate) -> User:
        # 检查邮箱是否已存在
        existing_user = await user_crud.get_user_by_email(self.db, user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        
        # 创建用户
        return await user_crud.create_user(self.db, user_data)

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = await user_crud.get_user_by_email(self.db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = await user_crud.get_user(self.db, user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return await user_crud.get_users(self.db, skip=skip, limit=limit)

    async def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        # 如果要更新邮箱，先检查新邮箱是否已被使用
        if user_data.email:
            existing_user = await user_crud.get_user_by_email(self.db, user_data.email)
            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=400,
                    detail="Email already registered"
                )

        updated_user = await user_crud.update_user(self.db, user_id, user_data)
        if not updated_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return updated_user

    async def delete_user(self, user_id: int) -> bool:
        # 可以添加额外的业务逻辑，比如检查用户是否有关联数据
        success = await user_crud.delete_user(self.db, user_id)
        if not success:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return True

    async def change_password(self, user_id: int, old_password: str, new_password: str) -> User:
        user = await user_crud.get_user(self.db, user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        
        # 验证旧密码
        if not verify_password(old_password, user.hashed_password):
            raise HTTPException(
                status_code=400,
                detail="Incorrect password"
            )
        
        # 更新密码
        user_update = UserUpdate(password=new_password)
        return await user_crud.update_user(self.db, user_id, user_update)
