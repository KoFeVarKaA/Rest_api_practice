from src.domain.user.repository import UserRepository, UserOrm
from src.domain.user.schema import UserSchema

from main import app

@app.get("/users", summary="Получить все пользователей из БД", tags=['Основные эндпоиты'])
def get_all():
    return UserRepository.select_users_all()

@app.get("/users/{user_id)}", summary="Получить пользователя по имени из БД", tags=['Основные эндпоиты'])
def get_by_name(user_id):
    return UserRepository.select_user_id(user_id)
    

@app.post("/users", summary="Добавить нового пользователя в БД", tags=['Основные эндпоиты'])
def create_user(new_user: UserSchema):
    UserRepository.insert_user(UserOrm(
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@app.delete("/users/{user_id}", summary="Удалить пользователя из БД", tags=['Основные эндпоиты'])
def delete_user(user_id):
    UserRepository.del_one(user_id)
    return {"message": "Пользователь успешно удален"}
