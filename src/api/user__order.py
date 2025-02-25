from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends

from src.domain.order.repository import OrderRepository, Order
from src.domain.user.repository import UserRepository
from src.domain.user__order.repository import UserOrderRepository

from src.domain.user__order.model import UserOrder

from src.domain.user.schema import UserSchema
from src.domain.order.schema import OrderSchema
from src.domain.user__order.schema import UserOrderSchema
from src.api.schemas import ResponseSchema

user__order_router = APIRouter(
    prefix="/UserOrder",
    tags=["UserOrder"],
)

@user__order_router.get("/", summary="Получить все данные из таблицы user__order")
async def get_all(
    repository : Annotated[UserOrderRepository, Depends(UserOrderRepository)]
) -> List[UserOrderSchema]:
    user__orders = await repository.get_all()
    return [UserOrderSchema(
                    id = user__order.id,
                    user_id = user__order.user_id,
                    order_id = user__order.order_id,                  
                ) for user__order in user__orders]

@user__order_router.get("/users", summary="Поиск всех пользователей по введенному id заказа")
async def get_users_by_order_id(
    order_id: int,
    repository_user: Annotated[UserRepository, Depends(UserRepository)],
    repository_user__order: Annotated[UserOrderRepository, Depends(UserOrderRepository)],
) -> List[UserSchema]: 
    user_ids = await repository_user__order.get_user_ids_by_order_id(order_id) 
    users = await repository_user.get_users_by_ids(user_ids) 
    return [UserSchema(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    age=user.age,
                ) for user in users]

@user__order_router.get("/orders", summary="Поиск всех заказов по введенному id пользователя")
async def get_orders_by_user_id(
    user_id: int,
    repository_order: Annotated[OrderRepository, Depends(OrderRepository)],
    repository_user__order: Annotated[UserOrderRepository, Depends(UserOrderRepository)],
) -> List[OrderSchema]:
    order_ids = await repository_user__order.get_order_ids_by_user_id(user_id)
    orders = await repository_order.get_orders_by_ids(order_ids)
    return [OrderSchema(
                        id=order.id,
                        name=order.name,
                        total_amount=order.total_amount,
                        status=order.status,
                        description=order.description,
                ) for order in orders]