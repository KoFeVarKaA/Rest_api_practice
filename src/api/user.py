from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.user.repository import UserRepository, User
from src.domain.user.schema import UserSchema

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@user_router.get("/", summary="Получить всех пользователей из БД")
async def get_all(
    repository : Annotated[UserRepository, Depends(UserRepository)]
) -> List[UserSchema]:
    users = await repository.get_all()
    return [UserSchema(
                        id=user.id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        age=user.age,                   
                ) for user in users]
 
@user_router.get("/{id}", summary="Получить пользователя по id из БД")
async def get_by_id(
    id: int,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> UserSchema:
    user = await repository.get_id(id)
    return UserSchema(
                        id=user.id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        age=user.age,                   
                    )

@user_router.get("/user_order/{order_id}", summary="Поиск всех пользователей по введенному id заказа")
async def get_users_by_order_id(
    order_id: int,
    repository: Annotated[UserRepository, Depends(UserRepository)]
) -> List[UserSchema]: 
    users = await repository.get_users_by_order_id(order_id) 
    return [UserSchema(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    age=user.age,
                ) for user in users]
    
@user_router.post("", summary="Добавить нового пользователя в БД")
async def create_user(
    new_user: UserSchema,
    repository: Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    await repository.insert(User(
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@user_router.delete("/{id}", summary="Удалить пользователя из БД")
async def delete_user(
    id: int,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    await repository.del_one(id)
    return {"message": "Пользователь успешно удален"}
