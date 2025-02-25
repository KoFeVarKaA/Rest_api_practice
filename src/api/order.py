from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.order.repository import OrderRepository, Order
from src.domain.user.repository import UserRepository
from src.domain.user__order.repository import UserOrderRepository

from src.domain.user__order.model import UserOrder

from src.domain.order.schema import OrderSchema
from src.domain.user__order.schema import UserOrderSchema
from src.api.schemas import ResponseSchema


order_router = APIRouter(
    prefix="/Orders",
    tags=["Orders"],
)

@order_router.get("/", summary="Получить все заказы из БД")
async def get_all(
    repository : Annotated[OrderRepository, Depends(OrderRepository)]
) -> List[OrderSchema]:
    orders = await repository.get_all()
    return [OrderSchema(
                        id=order.id,
                        name=order.name,
                        total_amount=order.total_amount,
                        status = order.status,
                        description = order.description,                                       
                ) for order in orders]
 
@order_router.get("/{id}", summary="Получить заказ по id из БД")
async def get_by_id(
    id: int,
    repository : Annotated[OrderRepository, Depends(OrderRepository)]
    ) -> OrderSchema:
    order = await repository.get_id(id)
    return OrderSchema(
                        id=order.id,
                        name=order.name,
                        total_amount=order.total_amount,
                        status = order.status,
                        description = order.description,                  
                    )
    
@order_router.post("", summary="Добавить новый заказ в БД")
async def create_order(
    user_id: int,
    new_order: OrderSchema,
    user__order : UserOrderSchema,
    repository: Annotated[OrderRepository, Depends(OrderRepository)],
    repository_user: Annotated[UserRepository, Depends(UserRepository)],
    repository_user__order: Annotated[UserOrderRepository, Depends(UserOrderRepository)],
    ) -> ResponseSchema:
    if repository_user.does_user_exist(user_id) == False:
        return ResponseSchema(code=404, message="Ошибка: пользователь не найден")
    else:
        order = Order(
                name=new_order.name,
                total_amount=new_order.total_amount,
                status = new_order.status,
                description = new_order.description,
        )
        await repository.insert(order)

        new_order_id = order.id

        await repository_user__order.insert(UserOrder(
                user_id=user_id,
                order_id=new_order_id,
        ))
        return ResponseSchema(code=200, message="Заказ успешно добавлен")

@order_router.delete("/{id}", summary="Удалить заказ из БД")
async def delete_order(
    id: int,
    repository : Annotated[OrderRepository, Depends(OrderRepository)]
    ) -> ResponseSchema:
    await repository.del_one(id)
    return ResponseSchema(code=200, message="Заказ успешно удален")
