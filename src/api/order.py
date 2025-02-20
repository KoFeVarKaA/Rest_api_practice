from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.order.repository import OrderRepository, Order
from src.domain.order.schema import OrderSchema

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
                        total_sum=order.total_sum,                    
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
                        total_sum=order.total_sum,                  
                    )
    
@order_router.post("", summary="Добавить новый заказ в БД")
async def create_order(
    new_order: OrderSchema,
    repository: Annotated[OrderRepository, Depends(OrderRepository)]
    ) -> Dict[str, Any]:
    await repository.insert(Order(
            name=new_order.name,
            total_sum=new_order.total_sum,
    ))
    return {"message": "Заказ успешно добавлен"}

@order_router.delete("/{id}", summary="Удалить заказ из БД")
async def delete_order(
    id: int,
    repository : Annotated[OrderRepository, Depends(OrderRepository)]
    ) -> Dict[str, Any]:
    await repository.del_one(id)
    return {"message": "Заказ успешно удален"}
