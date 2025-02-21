from sqlalchemy import select

from src.domain.order.model import Order
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
    async def insert(order : dict) -> None:
        async with session_factory() as session:
            session.add(order)
            await session.commit()

    @staticmethod
    async def get_id(order_id : int) -> Order: 
        async with session_factory() as session:
            order = await session.get(Order, {"id": order_id})
            return order
            
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