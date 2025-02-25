from sqlalchemy import select

from src.domain.user__order.model import UserOrder
from src.domain.user__order.schema import UserOrderSchema
from database import async_engine, session_factory



class UserOrderRepository:
    @staticmethod
    async def get_all() -> list[UserOrder]:
        async with session_factory() as session:
            query = select(UserOrder) 
            res = await session.execute(query)
            result = res.scalars().all()
            return result
        
    @staticmethod
    async def get_user_ids_by_order_id(order_id: int) -> list[int]: 
        async with session_factory() as session:
            query = (
                select(UserOrder.user_id)
                .filter(UserOrder.order_id == order_id)
            )
            res = await session.execute(query)
            user_ids = res.scalars().all()
            return user_ids
    
    @staticmethod
    async def get_order_ids_by_user_id(user_id: int) -> list[int]:
        async with session_factory() as session:
            query = (
                select(UserOrder.order_id)
                .filter(UserOrder.user_id == user_id)
            )
            res = await session.execute(query)
            order_ids = res.scalars().all()
            return order_ids

