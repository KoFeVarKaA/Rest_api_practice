from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.profession.model import Profession, ProfessionEnum
from src.domain.profession.repository import ProfessionRepository
from src.domain.user.repository import UserRepository, User
from src.domain.user.schema import UserSchema
from src.api.schemas import ResponseSchema

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
                        profession_id=user.profession_id                   
                ) for user in users]
 
@user_router.get("/get_by_id/{id}", summary="Получить пользователя по id из БД")
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
                        profession_id=user.profession_id                   
                    )

@user_router.get("/get_by_profession/{profession}", summary="Вернуть пользователей, которые относятся к определенной профессии")
async def get_users_by_profession_name(
    profession: ProfessionEnum,
    repository_user: Annotated[UserRepository, Depends(UserRepository)],
) -> List[UserSchema]:
    users = await repository_user.get_users_by_profession_name(profession) 
    return [UserSchema(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    age=user.age,
                    profession_id=user.profession_id
                ) for user in users]

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
                    profession_id=user.profession_id
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

@user_router.post("/profession/{user_id}/{profession}", summary="Присвоить пользователю профессию")
async def appropriate_profession(
    user_id: int,
    profession: ProfessionEnum,
    repository_user: Annotated[UserRepository, Depends(UserRepository)],
    repository_profession: Annotated[ProfessionRepository, Depends(ProfessionRepository)],
    ) -> ResponseSchema:
    user = await repository_user.does_user_exist(user_id)
    if isinstance(user, User):
        profession_id = await repository_profession.profession_to_id(profession)
        await repository_user.update_profession(user_id, profession_id)
        return ResponseSchema(code=200, message="Профессия успешно присвоена")   
    return ResponseSchema(code=404, message="Ошибка: пользователь не найден")

@user_router.delete("/{id}", summary="Удалить пользователя из БД")
async def delete_user(
    id: int,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    await repository.del_one(id)
    return {"message": "Пользователь успешно удален"}
