from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uvicorn

app = FastAPI()

class UserSchema(BaseModel):
    first_name: str
    last_name: str
    age: int


users_table = [
    {
        "first_name" : "user1", 
        "last_name" : "last_name1", 
        "age" : 130,
    },
     {
        "first_name" : "user2", 
        "last_name" : "last_name1", 
        "age" : 55,
    },
     {
        "first_name" : "user3", 
        "last_name" : "last_name666", 
        "age" : 20,
    },
]


@app.get("/users", summary="Получить все пользователей из БД", tags=['Основные эндпоиты'])
def get_all() -> list[UserSchema]:
    return users_table

@app.get("/users/{first_name}", summary="Получить пользователя по имени из БД", tags=['Основные эндпоиты'])
def get_by_name(first_name):
    for user in users_table:
        if user["first_name"] == first_name:
            return user
    

@app.post("/users", summary="Добавить нового пользователя в БД", tags=['Основные эндпоиты'])
def create_user(new_user: UserSchema):
    users_table.append(
        {
            "first_name" : new_user.first_name, 
            "last_name" : new_user.last_name, 
            "age" : new_user.age,
        },
    )
    return {"message": "Пользователь успешно добавлен"}

@app.delete("/users/{first_name}", summary="Удалить пользователя из БД", tags=['Основные эндпоиты'])
def delete_user(first_name):
    for i in range(len(users_table)):
        if users_table[i]["first_name"] == first_name:
            users_table.pop(i)
            break
    return {"message": "Пользователь успешно удален"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 