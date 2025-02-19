from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.user.repository import UserRepository, User
from src.domain.user.schema import UserSchema

# Функция для преобразования данных из модели SQLAlchemy в модель Pydantic
# def convert_to_pydantic(sqlalchemy_model: User) -> UserSchema:
#     return UserSchema(
#                         id=sqlalchemy_model.id,
#                         first_name=sqlalchemy_model.first_name,
#                         last_name=sqlalchemy_model.last_name,
#                         age=sqlalchemy_model.age
#                     )


user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@user_router.get("/", summary="Получить все пользователей из БД")
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
 
@user_router.get("/{id}", summary="Получить пользователя по имени из БД")
async def get_by_id(
    id,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> UserSchema:
    user = await repository.get_id(int(id))
    return UserSchema(
                        id=user.id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        age=user.age,                   
                    )
    
@user_router.post("", summary="Добавить нового пользователя в БД")
async def create_user(
    new_user: UserSchema,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    await repository.insert(User(


            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@user_router.delete("/{id}", summary="Удалить пользователя из БД")
async def delete_user(
    id,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    await repository.del_one(int(id))

    return {"message": "Пользователь успешно удален"}
