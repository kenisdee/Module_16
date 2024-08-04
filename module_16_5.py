from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Создание объекта Jinja2Templates с указанием папки шаблонов
templates = Jinja2Templates(directory="templates")

# Определение модели User
class User(BaseModel):
    id: int
    username: str
    age: int

# Инициализация списка users
users: List[User] = []

# POST запрос для добавления нового пользователя
@app.post("/users", response_model=User)
def add_user(user: User):
    if not users:
        new_id = 1
    else:
        new_id = max(user.id for user in users) + 1
    user.id = new_id
    users.append(user)
    return user

# Создание нескольких пользователей
add_user(User(id=1, username="UrbanUser", age=24))
add_user(User(id=2, username="UrbanTest", age=22))
add_user(User(id=3, username="Capybara", age=60))

# GET запрос для отображения списка пользователей
@app.get("/")
def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# GET запрос для отображения информации о конкретном пользователе
@app.get("/users/{user_id}")
def read_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})