from sqlalchemy import select

from src.domain.user.model import User
from src.domain.user.schema import UserSchema
from database import async_engine, session_factory


class UserRepository:

    @staticmethod
    async def del_one(user_id : int) -> None:
        async with session_factory() as session:
            obj = await session.get(User, user_id)
            await session.delete(obj)
            await session.commit()

    @staticmethod
    async def insert(user : dict) -> None:
        async with session_factory() as session:
            session.add(user)
            await session.commit()

    @staticmethod
    async def get_id(user_id : int) -> User: 
        async with session_factory() as session:
            user = await session.get(User, {"id": user_id})
            return user
            
    @staticmethod
    async def get_all() -> list[User]:
        async with session_factory() as session:
            query = select(User) 
            res = await session.execute(query)
            users = res.scalars().all()
            return users

    @staticmethod
    async def update(user_id : int, new_username : str) -> None:
        async with session_factory() as session:
            user = await session.get(User, user_id)
            user.username = new_username
            await session.commit()