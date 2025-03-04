from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.domain.user.model import User
from src.domain.order.model import Order
from src.domain.user__order.model import UserOrder
from src.domain.order.schema import OrderSchema
from database import async_engine, session_factory


class OrderRepository:

    @staticmethod
    async def del_one(order_id : int) -> None:
        async with session_factory() as session:
            obj = await session.get(Order, order_id)
            await session.delete(obj)
            await session.commit()

    @staticmethod
    async def insert(order : Order) -> None:
        async with session_factory() as session:
            session.add(order)
            await session.commit()
            await session.refresh(order)

    @staticmethod
    async def create_order_with_user(user_order : UserOrder) -> None:
        async with session_factory() as session:
            session.add(user_order)
            await session.commit()

    @staticmethod
    async def get_id(order_id : int) -> Order: 
        async with session_factory() as session:
            stmt = select(Order).where(Order.id == order_id)
            return (await session.scalars(stmt)).one_or_none()        
    
    @staticmethod
    async def get_orders_by_user_id(user_id: int) -> list[int]:
        async with session_factory() as session:
            stmt = select(User).where(User.id == user_id).options(selectinload(User.orders))
            return (await session.scalars(stmt)).one_or_none()
            
    @staticmethod
    async def get_all() -> list[Order]:
        async with session_factory() as session:
            query = select(Order) 
            res = await session.execute(query)
            orders = res.scalars().all()
            return orders

    @staticmethod
    async def update(order_id : int, new_ordername : str) -> None:
        async with session_factory() as session:
            order = await session.get(Order, order_id)
            Order.ordername = new_ordername
            await session.commit()