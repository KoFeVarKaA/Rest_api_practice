from fastapi import APIRouter
from src.domain.user.repository import UserRepository, User
from src.domain.user.schema import UserSchema
from src.domain.user.repository_test import UserRepository_test
UserRepository_test.create_tables()

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@user_router.get("/users", summary="Получить все пользователей из БД")
def get_all():
    return UserRepository.get_all()

@user_router.get("/users/{user_id)}", summary="Получить пользователя по имени из БД")
def get_by_name(user_id):
    return UserRepository.get_id(user_id)
    

@user_router.post("/users", summary="Добавить нового пользователя в БД")
def create_user(new_user: UserSchema):
    UserRepository.insert(User(
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@user_router.delete("/users/{user_id}", summary="Удалить пользователя из БД")
def delete_user(user_id):
    UserRepository.del_one(user_id)
    return {"message": "Пользователь успешно удален"}
