from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Определение модели User
class User(BaseModel):
    id: int
    username: str
    age: int

# Инициализация списка users
users: List[User] = []

# GET запрос для получения всех пользователей
@app.get("/users", response_model=List[User])
def get_users():
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
def add_user(username: str, age: int):
    if not users:
        new_id = 1
    else:
        new_id = max(user.id for user in users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")