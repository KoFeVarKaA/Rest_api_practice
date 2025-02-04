from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn

from src.domain.user.repository import UserRepository, UsersOrm
from src.domain.user.schema import UserSchema

app = FastAPI()

UserRepository.create_tables()
UserRepository.insert_users()


@app.get("/users", summary="Получить все пользователей из БД", tags=['Основные эндпоиты'])
def get_all():
    return UserRepository.select_users_all()

@app.get("/users/{user_id)}", summary="Получить пользователя по имени из БД", tags=['Основные эндпоиты'])
def get_by_name(user_id):
    return UserRepository.select_user_id(user_id)
    

@app.post("/users", summary="Добавить нового пользователя в БД", tags=['Основные эндпоиты'])
def create_user(new_user: UserSchema):
    UserRepository.insert_user(UsersOrm(
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@app.delete("/users/{user_id}", summary="Удалить пользователя из БД", tags=['Основные эндпоиты'])
def delete_user(user_id):
    UserRepository.del_one(user_id)
    return {"message": "Пользователь успешно удален"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 