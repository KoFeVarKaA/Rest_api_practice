from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends
from src.domain.user.repository import UserRepository, User
from src.domain.user.schema import UserSchema

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@user_router.get("/", summary="Получить все пользователей из БД")
def get_all(
    repository : Annotated[UserRepository, Depends(UserRepository)]
) -> List[UserSchema]:
    return repository.get_all()
 
@user_router.get("/{user_id)}", summary="Получить пользователя по имени из БД")
def get_by_id(
    user_id,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> UserSchema:
    return repository.get_id(user_id)
    
@user_router.post("", summary="Добавить нового пользователя в БД")
def create_user(
    new_user: UserSchema,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    repository.insert(User(

            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@user_router.delete("/{user_id}", summary="Удалить пользователя из БД")
def delete_user(
    user_id,
    repository : Annotated[UserRepository, Depends(UserRepository)]
    ) -> Dict[str, Any]:
    repository.del_one(user_id)
    return {"message": "Пользователь успешно удален"}
