from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn

from database import SyncORM, UsersOrm

app = FastAPI()

SyncORM.create_tables()
SyncORM.insert_users()

class UserSchema(BaseModel):
    first_name: str
    last_name: str
    age: int

@app.get("/users", summary="Получить все пользователей из БД", tags=['Основные эндпоиты'])
def get_all():
    return SyncORM.select_users_all()

@app.get("/users/{user_id)}", summary="Получить пользователя по имени из БД", tags=['Основные эндпоиты'])
def get_by_name(user_id):
    return SyncORM.select_user_id(user_id)
    

@app.post("/users", summary="Добавить нового пользователя в БД", tags=['Основные эндпоиты'])
def create_user(new_user: UserSchema):
    SyncORM.insert_user(UsersOrm(
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            age=new_user.age,
    ))
    return {"message": "Пользователь успешно добавлен"}

@app.delete("/users/{user_id}", summary="Удалить пользователя из БД", tags=['Основные эндпоиты'])
def delete_user(user_id):
    SyncORM.del_one(user_id)
    return {"message": "Пользователь успешно удален"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 